import pygame
from pygame import Surface
from pygame.image import *
import os
import sys, getopt

def scaleImageInFile(path):
	print "loading", path
	try:
		sourceImage = pygame.image.load(path)
	except:
		print 'An error occurred loading image \"%s\"' % path
		sys.exit(2)
	# copy the source image into the target image, though we're about to overwrite it we want its format
	targetImage = Surface((sourceImage.get_width() * 2, sourceImage.get_height() * 2), sourceImage.get_flags(), sourceImage)
	for x in range(0, sourceImage.get_width()):
		for y in range(0, sourceImage.get_height()):
			# determine neighboring pixels
			# TODO check diagonal edges
			#a = sourceImage.get_at((x - 1, y - 1)) if y > 0 and x > 0 else sourceImage.get_at((x, y))
			b = sourceImage.get_at((x, y - 1)) if y > 0 else sourceImage.get_at((x, y))
			#c = sourceImage.get_at((x + 1, y - 1)) if y > 0 and (x + 1) < sourceImage.get_width() else sourceImage.get_at((x, y))
			d = sourceImage.get_at((x - 1, y)) if x > 0 else sourceImage.get_at((x, y))
			e = sourceImage.get_at((x, y))
			f = sourceImage.get_at((x + 1, y)) if (x + 1) < sourceImage.get_width() else sourceImage.get_at((x, y))
			#g = sourceImage.get_at((x - 1, y + 1)) if (y + 1) < sourceImage.get_height() and x > 0 else sourceImage.get_at((x, y))
			h = sourceImage.get_at((x, y + 1)) if (y + 1) < sourceImage.get_height() else sourceImage.get_at((x, y))
			#i = sourceImage.get_at((x + 1, y + 1)) if (y + 1) < sourceImage.get_height() and (x + 1) < sourceImage.get_width() else sourceImage.get_at((x, y))
			
			if b != h and d != f:
				e0 = d if d == b else e
				e1 = f if b == f else e
				e2 = d if d == h else e
				e3 = f if h == f else e
			else:
				e0 = e
				e1 = e
				e2 = e
				e3 = e
			
			# figure out target coordinates for e0, e1, e2, e3
			targetImage.set_at((x * 2, y * 2), e0)
			targetImage.set_at((x * 2 + 1, y * 2), e1)
			targetImage.set_at((x * 2, y * 2 + 1), e2)
			targetImage.set_at((x * 2 + 1, y * 2 + 1), e3)
			
	# write image back to file
	filename, extension = os.path.splitext(path)
	newPath = filename + '.scaled2x' + extension
	pygame.image.save(targetImage, newPath)
			
	# print happy message
	print "Scaled up version is at", newPath

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], '')
	except getopt.error, msg:
		print msg
		sys.exit(2)
	for arg in args:
		# process each argument as a file, open it, scale2x and output it as .scaled
		scaleImageInFile(arg)

if __name__ == '__main__': main()