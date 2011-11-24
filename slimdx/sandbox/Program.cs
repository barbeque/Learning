using System;
using System.Drawing;
using System.Windows.Forms;
using SlimDX;
using SlimDX.Direct3D10;
using SlimDX.DXGI;
using SlimDX.Windows;
using Device = SlimDX.Direct3D10.Device;

namespace sandbox
{
    class Program : IDisposable
    {
        private RenderForm _form;
        private SwapChain _swapChain;
        private Device _device;
        private Texture2D _renderTexture;
        private RenderTargetView _renderTargetView;
        private Viewport _viewport;

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
            _form = new RenderForm("SlimDX Sandbox");

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
                                                                Width = _form.ClientSize.Width,
                                                                Height = _form.ClientSize.Height,
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
                                      Flags = SwapChainFlags.None,
                                      SwapEffect = SwapEffect.Discard
                                  };

            // Create device
            SlimDX.Direct3D10_1.Device1.CreateWithSwapChain(null, DriverType.Hardware, DeviceCreationFlags.None,
                                                            description, out _device, out _swapChain);

            Texture2DDescription renderTargetTextureDescription = new Texture2DDescription
                                                                      {
                                                                          Width = _form.ClientSize.Width,
                                                                          Height = _form.ClientSize.Height,
                                                                          Format = description.ModeDescription.Format,
                                                                          MipLevels = 1,
                                                                          ArraySize = 1,
                                                                          SampleDescription =
                                                                              new SampleDescription(1, 0),
                                                                          Usage = ResourceUsage.Default,
                                                                          CpuAccessFlags = CpuAccessFlags.None,
                                                                          BindFlags =
                                                                              BindFlags.RenderTarget |
                                                                              BindFlags.ShaderResource,
                                                                          OptionFlags = ResourceOptionFlags.Shared

                                                                      };

            _renderTexture = new Texture2D(_device, renderTargetTextureDescription);
            _renderTargetView = new RenderTargetView(_device, _renderTexture);

            // TODO {Mike Stedman - Nov 23, 2011} add depth stuff

            _viewport = new Viewport(0, 0, _form.ClientSize.Width, _form.ClientSize.Height, 0.0f, 1.0f);
            _device.Rasterizer.SetViewports(_viewport);
			_device.OutputMerger.SetTargets(_renderTargetView);
        }

        public void RenderFrame()
        {
            _device.ClearRenderTargetView(_renderTargetView, Color.White);
            _swapChain.Present(0, PresentFlags.None);
        }

        #region Implementation of IDisposable

        /// <summary>
        /// Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.
        /// </summary>
        /// <filterpriority>2</filterpriority>
        public void Dispose()
        {
            TryDisposing(_device);
            TryDisposing(_renderTargetView);
            TryDisposing(_renderTexture);
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
