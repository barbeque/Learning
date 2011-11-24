import pygame, sys
from pygame.locals import *

def makePalette():
	palette = []
	maxR = 0
	maxG = 0
	maxB = 0

	for i in range(0, 256):
# 2 bits of blue
		b = i & 0x3
# 3 bits of green
		g = (i & 0x1c) >> 2
# 3 bits of red
		r = (i & 0xe0) >> 5

		r = (r / 7.0) * 255
		g = (g / 7.0) * 255
		b = (b / 3.0) * 255

		maxR = max(r, maxR)
		maxG = max(g, maxG)
		maxB = max(b, maxB)

		palette.append(pygame.Color(int(r), int(g), int(b)))

	print "maximum values of each rgb channel:", maxR, maxG, maxB
	return palette

def cyclePalette(palette, amount):
	newPalette = list(palette)
	for x in range(0, len(palette)):
		newPalette[x] = palette[(x + amount) % len(palette)]
	return newPalette

palette = makePalette()

pygame.init()
surface = pygame.display.set_mode((512, 384))
pygame.display.set_caption('palettes')

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			palette = cyclePalette(palette, 1)

	boxSize = 16
	boxGap = 1

	x = 0
	y = 0

	for c in palette:
		pygame.draw.rect(surface, c, Rect(x, y, boxSize, boxSize))

		if x + 16 + boxGap > surface.get_width():
			x = 0
			y += boxSize
		else:
			x += boxSize + boxGap

	pygame.display.update()
