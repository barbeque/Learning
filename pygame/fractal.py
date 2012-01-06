import pygame, math

def draw(screen):
	drawBranch(screen, 10, 320, 240, 40, 0)
	
def drawBranch(screen, depth, originX, originY, length, theta):
	destinationX = originX + length * math.cos(theta)
	destinationY = originY + length * math.sin(theta)
	color = pygame.Color('red')
	color.r = (int)((float(depth) / 10) * 255);
	pygame.draw.line(screen, color, (originX, originY), (destinationX, destinationY))
	
	if depth > 1:
		drawBranch(screen, depth - 1, destinationX, destinationY, length * 0.95, theta + 1.2)
		drawBranch(screen, depth - 1, destinationX, destinationY, length * 0.95, theta - 1.2)
		
def main():
	screen = pygame.display.set_mode((640, 480))
	running = True
	
	while running:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			running = False
		
		screen.fill((0, 0, 0))
			
		draw(screen)
		
		pygame.display.flip()
	
	
if __name__ == '__main__': main()