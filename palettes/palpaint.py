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

def drawSelectionBox(surface, x, y, boxSize):
	color = pygame.Color('purple')
	width = 2

	# top: x, y, to (x + boxSize, y + w)
	pygame.draw.rect(surface, color, Rect(x, y, boxSize, width))
	# bottom: x, y + boxSize to (x + boxSize, y + boxSize - w)
	pygame.draw.rect(surface, color, Rect(x, y + boxSize - width, boxSize, width))
	# left: x, y to x + width, y + boxSize
	pygame.draw.rect(surface, color, Rect(x, y, width, boxSize))
	# right: x + boxSize, y to x + boxSize - w, y + boxSize
	pygame.draw.rect(surface, color, Rect(x + boxSize - width, y, width, boxSize))

def drawPalettePicker(surface, boxSize, boxGap, selectedIndex):
	x = 0
	y = 0
	index = 0

	for c in palette:
		pygame.draw.rect(surface, c, Rect(x, y, boxSize, boxSize))

		if index == selectedIndex:
			# draw selection box
			drawSelectionBox(surface, x, y, boxSize)

		if x + (boxSize + boxGap)*2 >= surface.get_width(): # x2 to make sure the next rect is COMPLETELY CONTAINED within the screen
			x = 0
			y += boxSize + boxGap
		else:
			x += boxSize + boxGap
		index = index + 1

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
pygame.display.set_caption('palpaint')

isRunning = True
paletteOpen = False
boxSize = 16
boxGap = 1

# the colour that the mouse is painting with
paintIndex = 16

width, height = surface.get_size()

spriteBuffer = []
for r in range(height / (boxSize + boxGap)):
	row = []
	for c in range(width / (boxSize + boxGap)):
		row.append(0) # todo random pixels
	spriteBuffer.append(row)

while isRunning:
	pygame.draw.rect(surface, pygame.Color('black'), Rect(0, 0, width, height))

	for event in pygame.event.get():
		if event.type == QUIT:
			isRunning = False
		elif event.type == KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				isRunning = False
			elif event.key == pygame.K_p:
				paletteOpen = not paletteOpen
			else:
				palette = cyclePalette(palette, 1)
		elif event.type == MOUSEBUTTONDOWN:
			mouseX, mouseY = event.pos
			cursorX = mouseX / (boxSize + boxGap)
			cursorY = mouseY / (boxSize + boxGap)
			if paletteOpen:
				tilesPerRow = (width / (boxSize + boxGap))
				paintIndex = cursorY * (width / (boxSize + boxGap)) + cursorX
			else:
				# TODO bounds check
				spriteBuffer[cursorY][cursorX] = paintIndex

	if paletteOpen:
		drawPalettePicker(surface, boxSize, boxGap, paintIndex)
	else:
		drawBuffer(surface, palette, spriteBuffer, boxSize, boxGap)

	pygame.display.update()
