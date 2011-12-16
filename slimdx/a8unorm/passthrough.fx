Texture2D inputTexture;
SamplerState inputTextureSampler {
	Filter = MIN_MAG_MIP_LINEAR;
	AddressU = Wrap;
	AddressV = Wrap;
};

float4 VShader(float4 position : POSITION) : SV_POSITION {
	return position;
}

float4 PShader(float4 position : SV_POSITION) : SV_Target {
	float alpha = inputTexture.Sample(inputTextureSampler, float2(position.x * 100.0, position.y * 100.0))[3];
	return float4(alpha, 0.0f, 0.0f, 1.0f);
}