# tests the raytrace code
import raytrace

c = raytrace.Camera()

# test to make sure that for all pixels on our screen stuff makes sense
width = 640
height = 480

rays = raytrace.getRaysForScreen(width, height, c)

# make sure we got the right number of rays
assert(len(rays) == height - 1)
for y in range(height - 1):
	assert(len(rays[y]) == (width - 1))