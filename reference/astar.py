import sys
import math

# Simple tile map with A* pathfinding
class AStarMap:
	def __init__(self, width = 10, height = 10):
		self.width = width
		self.height = height

		# define 2D array
		self.data = []
		for y in xrange(self.height):
			self.data.append([])
			for x in xrange(self.width):
				self.data[y].append(False)
	def setCollidable(self, x, y, isCollidable):
		self.data[y][x] = isCollidable
	def isCollidable(self, x, y):
		return self.data[y][x]
	def pathFind(self, startX, startY, goalX, goalY):
		# add start node to open list
		open = [ PathStep(startX, startY, None, 0, 0) ]
		closed = []

		isDone = False
		while not isDone:
			# find the lowest F-cost in the open list
			current = self.getLowestFCost(open)

			if current.x == goalX and current.y == goalY:
				# holy crap we found the goal!
				isDone = True
				backwardsPath = current.makePathBackToStart()
				# reverse in place
				backwardsPath.reverse()
				return backwardsPath
	
			# get unoccupied adjacent tiles
			adjacents = self.getAdjacentNodes(current.x, current.y)
			# get the additional G and H scores for these adjacents
			for adjacent in adjacents:
				x = adjacent[0]
				y = adjacent[1]
				g = self.calculateGCost(current.x, current.y, x, y) + current.gCost
				h = self.calculateHCost(goalX, goalY, x, y) + current.hCost
				# add to open list
				if not self.inList(x, y, open) and not self.inList(x, y, closed):
					open.append( PathStep(x, y, current, g, h) )
				# TODO check adjacent squares already on the open list to see if this path
				# is a faster way to get to that one

			# put the current one in the closed list
			closed.append(current)
			open.remove(current)

			if len(open) < 1:
				# no path seems to exist
				return None
	def getAdjacentNodes(self, startX, startY):
		adjacents = []
		for testX in range(startX - 1, startX + 2):
			if testX < 0 or testX >= self.width:
				continue		

			for testY in range(startY - 1, startY + 2):
				if testY < 0 or testY >= self.height:
					continue
				if not self.isCollidable(testX, testY) and not (testX == startX and testY == startY):
					adjacents.append( (testX, testY) )
		return adjacents
	def calculateGCost(self, startX, startY, endX, endY):
		# only works on adjacents
		xDistance = math.fabs(startX - endX)
		yDistance = math.fabs(startY - endY)

		assert xDistance < 2
		assert yDistance < 2

		if xDistance == 0 and yDistance == 1:
			# vertical
			return 10
		elif xDistance == 1 and yDistance == 0:
			# horizontal
			return 10
		else:
			# diagonal
			return 14
	def calculateHCost(self, startX, startY, endX, endY):
		xDistance = math.fabs(startX - endX)
		yDistance = math.fabs(startY - endY)

		return (xDistance + yDistance) * 10
	def getLowestFCost(self, pathStepList):
		lowest = sys.maxint
		bestStep = None

		assert len(pathStepList) > 0

		for pathStep in pathStepList:
			if pathStep.getFCost() < lowest:
				bestStep = pathStep
				lowest = pathStep.getFCost()
		return bestStep
	def inList(self, x, y, pathStepList):
		for pathStep in pathStepList:
			if pathStep.x == x and pathStep.y == y:
				return True
		return False

class PathStep:
	def __init__(self, x, y, parent, gCost, hCost):
		self.x = x
		self.y = y
		self.parent = parent
		self.gCost = gCost
		self.hCost = hCost
	def getFCost(self):
		return self.gCost + self.hCost
	def makePathBackToStart(self):
		path = [ (self.x, self.y) ]
		isDone = False
		
		current = self.parent
		while not isDone:
			if current == None:
				# no where else to go
				isDone = True
				break
			else:
				# add this node to path
				path.append( (current.x, current.y) )
				# iterate again
				current = current.parent
		return path

def main():
	demoMap = AStarMap(7, 5)
	# make a wall
	demoMap.setCollidable(3, 1, True)
	demoMap.setCollidable(3, 2, True)
	demoMap.setCollidable(3, 3, True)
	# goal time, walk around that wall
	solvedPath = demoMap.pathFind(1, 2, 5, 2)

	if not solvedPath == None:
		for step in solvedPath:
			print step
	else:
		print "No solution :("

if __name__ == '__main__':
	main()
