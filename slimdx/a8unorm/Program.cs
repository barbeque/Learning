﻿using System;
using System.Windows.Forms;
using SlimDX;
using SlimDX.D3DCompiler;
using SlimDX.Direct3D10;
using SlimDX.DXGI;
using SlimDX.Windows;
using Buffer = SlimDX.Direct3D10.Buffer;
using Device = SlimDX.Direct3D10.Device;
using Format = SlimDX.DXGI.Format;
using PresentFlags = SlimDX.DXGI.PresentFlags;
using Resource = SlimDX.Direct3D10.Resource;
using SwapChain = SlimDX.DXGI.SwapChain;
using SwapEffect = SlimDX.DXGI.SwapEffect;
using Usage = SlimDX.DXGI.Usage;
using Viewport = SlimDX.Direct3D10.Viewport;

namespace a8unorm
{
	class Program : IDisposable
	{
		private RenderForm _form;
		private SwapChain _swapChain;
		private Device _device;
		private RenderTargetView _renderTargetView;
		private Viewport _viewport;
		private DepthStencilState _depthStencilState;
		private DepthStencilView _depthStencilView;
		private Texture2D _depthBuffer;
		private InputLayout _inputLayout;
	    private RasterizerState _rasterizerState;

        private Texture2D _unormTexture;
        private ShaderResourceView _unormTextureView;

        private Buffer _vertexBuffer;
	    private Buffer _closerTriangleBuffer;

		private VertexShader _vertexShader;
		private PixelShader _pixelShader;

		#region Boilerplate

		/// <summary>
		/// The main entry point for the application.
		/// </summary>
		[STAThread]
		static void Main()
		{
			Application.EnableVisualStyles();
			Application.SetCompatibleTextRenderingDefault(false);

			using (var p = new Program())
			{
				p.Run();
			}
		}

		public void Run()
		{
			_form = new RenderForm("SlimDX Sandbox II: Secret of the Ooze");

			Initialize();

			MessagePump.Run(_form, RenderFrame);
		}

		#endregion

		public void Initialize()
		{
			var description = new SwapChainDescription
								  {
									  BufferCount = 1,
									  Usage = Usage.RenderTargetOutput,
									  OutputHandle = _form.Handle,
									  IsWindowed = true,
									  ModeDescription = new ModeDescription
															{
																Width = 0,
																Height = 0,
																Format = Format.R8G8B8A8_UNorm,
																RefreshRate = new Rational(60, 1),
																Scaling = DisplayModeScaling.Unspecified,
																ScanlineOrdering = DisplayModeScanlineOrdering.Unspecified
															},
									  SampleDescription = new SampleDescription
															  {
																  Count = 1,
																  Quality = 0
															  },
									  Flags = SwapChainFlags.AllowModeSwitch,
									  SwapEffect = SwapEffect.Discard
								  };

			// Create device
			SlimDX.Direct3D10_1.Device1.CreateWithSwapChain(null, DriverType.Hardware, DeviceCreationFlags.None,
															description, out _device, out _swapChain);

			using (var resource = Resource.FromSwapChain<Texture2D>(_swapChain, 0))
			{
				_renderTargetView = new RenderTargetView(_device, resource);
			}

			InitializeDepthBuffer();
			InitializeMeshes();
            InitializeWritableTexture();
			InitializeShaders("passthrough.fx");

			_viewport = new Viewport(0, 0, _form.ClientSize.Width, _form.ClientSize.Height, 0.0f, 1.0f);
			_device.Rasterizer.SetViewports(_viewport);
			_device.OutputMerger.SetTargets(_depthStencilView, _renderTargetView);

		    _rasterizerState = RasterizerState.FromDescription(_device, new RasterizerStateDescription
		                                                                    {
                                                                                IsDepthClipEnabled = false,
                                                                                FillMode = FillMode.Solid,
                                                                                CullMode = CullMode.None
		                                                                    });
		    _device.Rasterizer.State = _rasterizerState;

			_form.UserResized += (sender, e) =>
									 {
										 _renderTargetView.Dispose();

										 _swapChain.ResizeBuffers(2, 0, 0, Format.R8G8B8A8_UNorm,
																  SwapChainFlags.AllowModeSwitch);
										 using (var resource = Resource.FromSwapChain<Texture2D>(_swapChain, 0))
										 {
											 _renderTargetView = new RenderTargetView(_device, resource);
										 }

										 InitializeDepthBuffer();
                                         InitializeWritableTexture();

										 _device.OutputMerger.SetTargets(_depthStencilView, _renderTargetView);
									 };
		}

        private void InitializeWritableTexture()
        {
            TryDisposing(_unormTexture);
            TryDisposing(_unormTextureView);

            const int size = 32;
            _unormTexture = new Texture2D(_device, new Texture2DDescription {
                BindFlags = BindFlags.ShaderResource,
                Width = size,
                Height = size,
                Format = Format.A8_UNorm,
                OptionFlags = ResourceOptionFlags.None,
                CpuAccessFlags = CpuAccessFlags.Write,
                Usage = ResourceUsage.Dynamic,
                SampleDescription = new SampleDescription(count: 1, quality: 0),
                ArraySize = 1,
                MipLevels = 1 }
                );
            _unormTextureView = new ShaderResourceView(_device, _unormTexture);
        }

		private void InitializeDepthBuffer()
		{
            TryDisposing(_depthStencilView);
            TryDisposing(_depthBuffer);

			_depthStencilState = DepthStencilState.FromDescription(_device, new DepthStencilStateDescription
																				{
																					IsDepthEnabled = true,
																					DepthComparison =
																						Comparison.LessEqual
																				});
			
			_depthBuffer = new Texture2D(_device, new Texture2DDescription
													  {
														  Width = _form.ClientSize.Width,
														  Height = _form.ClientSize.Height,
														  Usage = ResourceUsage.Default,
														  BindFlags = BindFlags.DepthStencil,
														  ArraySize = 1,
														  CpuAccessFlags = CpuAccessFlags.None,
														  Format = Format.D32_Float,
														  MipLevels = 1,
														  OptionFlags = ResourceOptionFlags.None,
														  SampleDescription = new SampleDescription(1, 0)
													  });

			_depthStencilView = new DepthStencilView(_device, _depthBuffer);
		}

		/// <summary>
		/// Creates the meshes we will display
		/// </summary>
		private void InitializeMeshes()
		{
			var vertices = new DataStream(12 * 3, canRead: true, canWrite: true);
			vertices.Write(new Vector3(0.0f, 0.5f, 0.5f));
			vertices.Write(new Vector3(0.5f, -0.5f, 0.5f));
			vertices.Write(new Vector3(-0.5f, -0.5f, 0.5f));
			vertices.Position = 0; // always remember to rewind

			_vertexBuffer = new Buffer(_device, vertices, 12 * 3, ResourceUsage.Default, BindFlags.VertexBuffer,
									   CpuAccessFlags.None, ResourceOptionFlags.None);

			_device.InputAssembler.SetPrimitiveTopology(PrimitiveTopology.TriangleList);
			_device.InputAssembler.SetVertexBuffers(0, new VertexBufferBinding(_vertexBuffer, 12, 0));

		    var closerVertices = new DataStream(12 * 3, true, true);
            closerVertices.Write(new Vector3(0.0f, -0.5f, 0.3f));
            closerVertices.Write(new Vector3(0.5f, 0.5f, 0.3f));
            closerVertices.Write(new Vector3(-0.5f, 0.5f, 0.8f));
            closerVertices.Position = 0;

		    _closerTriangleBuffer = new Buffer(_device, closerVertices, 12 * 3, ResourceUsage.Default, BindFlags.VertexBuffer,
		                                       CpuAccessFlags.None, ResourceOptionFlags.None);
		}

		/// <summary>
		/// Creates the matrices we will use to display
		/// </summary>
		private void InitializeMatrices()
		{
		}

		private void InitializeShaders(string shaderName)
		{
			TryDisposing(_vertexShader);
			TryDisposing(_pixelShader);

			using (var bytecode = ShaderBytecode.CompileFromFile(shaderName, "VShader", "vs_4_0", ShaderFlags.None, EffectFlags.None))
			{
				_inputLayout = new InputLayout(_device, bytecode,
											   new[] {new InputElement("POSITION", 0, Format.R32G32B32_Float, 0, 0)});
				_device.InputAssembler.SetInputLayout(_inputLayout);

				_vertexShader = new VertexShader(_device, bytecode);
			}
			using (var bytecode = ShaderBytecode.CompileFromFile(shaderName, "PShader", "ps_4_0", ShaderFlags.None, EffectFlags.None))
			{
				_pixelShader = new PixelShader(_device, bytecode);
			}

			_device.VertexShader.Set(_vertexShader);
			_device.PixelShader.Set(_pixelShader);
		}

		public void RenderFrame()
		{
			_device.ClearDepthStencilView(_depthStencilView, DepthStencilClearFlags.Depth, 1.0f, 0);
			_device.ClearRenderTargetView(_renderTargetView, new Color4(0.5f, 0.5f, 1.0f));

            // Write to the texture view
            DataStream textureStream = _unormTexture.Map(0, MapMode.WriteDiscard, SlimDX.Direct3D10.MapFlags.None).Data;
            for (int i = 0; i < textureStream.Length; i++)
            {
                byte toWrite = (i % 2 == 0) ? (byte)0 : (byte)125;
                textureStream.Write(toWrite);
            }
            textureStream.Position = 0;
            textureStream.Close();
            _unormTexture.Unmap(0);

            // Send our texture to the view            
            _device.PixelShader.SetShaderResource(_unormTextureView, 0); // better way to do this surely

			// Draw once, then flip, then draw again
            _device.InputAssembler.SetVertexBuffers(0, new VertexBufferBinding(_vertexBuffer, 12, 0));
			_device.Draw(3, 0);

            _device.InputAssembler.SetVertexBuffers(0, new VertexBufferBinding(_closerTriangleBuffer, 12, 0));
            _device.Draw(3, 0);

			_swapChain.Present(0, PresentFlags.None);
		}

		#region Implementation of IDisposable

		/// <summary>
		/// Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.
		/// </summary>
		/// <filterpriority>2</filterpriority>
		public void Dispose()
		{
		    TryDisposing(_rasterizerState);
			TryDisposing(_pixelShader);
			TryDisposing(_vertexShader);
			TryDisposing(_device);
			TryDisposing(_vertexBuffer);
		    TryDisposing(_closerTriangleBuffer);
			TryDisposing(_renderTargetView);
			TryDisposing(_depthBuffer);
			TryDisposing(_depthStencilView);
			TryDisposing(_depthStencilState);
            TryDisposing(_unormTexture);
            TryDisposing(_unormTextureView);
			TryDisposing(_inputLayout);
			TryDisposing(_swapChain);
			TryDisposing(_form);
		}

		private void TryDisposing(IDisposable disposable)
		{
			if (disposable != null)
			{
				disposable.Dispose();
			}
		}

		#endregion
	}
}
