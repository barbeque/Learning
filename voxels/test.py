# tests the raytrace code
import raytrace

c = raytrace.Camera()

# test to make sure that for all pixels on our screen stuff makes sense
width = 640
height = 480

for x in range(width - 1):
	for y in range(height - 1):
		r = raytrace.makeRayForPixel(x, y, width, height, c)