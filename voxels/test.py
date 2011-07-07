# tests the raytrace code
import raytrace

c = raytrace.Camera()

# test to make sure that for all pixels on our screen stuff makes sense
width = 640
height = 480

rays = raytrace.getRaysForScreen(width, height, c)