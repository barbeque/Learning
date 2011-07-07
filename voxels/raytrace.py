import math

class Vector():
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def normalize(self):
		length = self.length()
		self.x /= length
		self.y /= length
		self.z /= length
	def getNormalized(self):
		output = Vector(self.x, self.y, self.z)
		output.normalize()
		return output
	def length(self):
		return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))
	def cross(self, otherV):
		cx = (self.y * otherV.z) - (self.z * otherV.y)
		cy = (self.z * otherV.x) - (self.x * otherV.z)
		cz = (self.x * otherV.y) - (self.y * otherV.x)
		return Vector(cx, cy, cz)
	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
		# todo operator overloading
	def __add__(self, otherV):
		return Vector(self.x + otherV.x, self.y + otherV.y, self.z * otherV.z)
	def __sub__(self, otherV):
		return Vector(self.x - otherV.x, self.y - otherV.y, self.z - otherV.z)
		
class Ray:
	def __init__(self, origin, direction):
		self.origin = origin
		self.direction = direction.getNormalized()
		
class Camera:
	def __init__(self):
		self.position = Vector(0.0, 0.0, 0.0)
		self.lookAt = Vector(0.0, 0.0, 100.0)
		self.up = Vector(0.0, 1.0, 0.0)

def makeRayForPixel(x, y, width, height, camera):
	# set up the coordinate system (should cache this!)
	n = (camera.position - camera.lookAt).getNormalized()
	u = camera.up.cross(n).getNormalized()
	v = n.cross(u).getNormalized()
	viewPortCentre = camera.position - n
	
	# figure out constants
	hfov = math.pi / 3.5
	vfov = hfov * float(height) / float(width)
	# TODO look into the math basis for this code
	pixelWidth = 2.0 * math.tan(hfov * 0.5) / width
	pixelHeight = 2.0 * math.tan(vfov * 0.5) / height
	
	# use this information
	rayPoint = (u * (x - width / 2.0) * pixelWidth) + (v * (y - height / 2.0) * pixelHeight)
	rayDirection = (rayPoint - camera.position).getNormalized()
	
	ray = Ray(rayPoint, rayDirection)
	return ray
