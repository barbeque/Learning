import pygame, sys
from pygame.locals import *

def makePalette():
	palette = []

	for i in range(0, 256):
		if (i / 4) % 2 == 0:
			b = 0
			g = 0
			r = 255
		else:
			r = 255
			g = 255
			b = 255

		palette.append(pygame.Color(int(r), int(g), int(b)))

	return palette

def cyclePalette(palette, amount):
	newPalette = list(palette)
	for x in range(0, len(palette)):
		newPalette[x] = palette[(x + amount) % len(palette)]
	return newPalette

def drawBuffer(surface, palette, buffer, boxSize, boxGap):
	x = 0
	y = 0
	for row in buffer:
		for value in row:
			# dereference palette index to real colour
			pixelColor = palette[value]
			# blit that pixel
			pygame.draw.rect(surface, pixelColor, Rect(x, y, boxSize, boxSize))
			x += boxSize + boxGap
		x = 0
		y += boxSize + boxGap

palette = makePalette()

pygame.init()
surface = pygame.display.set_mode((512, 384))
pygame.display.set_caption('palettes')

# generate buffer
buffer = []
for row in range(0, 64):
	rowBuffer = []
	for column in range(0, 64):
		if (row / 4) % 2 == 0:
			rowBuffer.append(column)
		else:
			rowBuffer.append(column + 4)
	buffer.append(rowBuffer)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			palette = cyclePalette(palette, 1)

	boxSize = 2
	boxGap = 1

	drawBuffer(surface, palette, buffer, boxSize, boxGap)

	pygame.display.update()