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
		
class Ray:
	def __init__(self, origin, direction):
		self.origin = origin
		self.direction = direction.getNormalized()