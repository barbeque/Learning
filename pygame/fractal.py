import pygame, math, random

def draw(screen):
	theta = -math.pi / 2
	drawBranch(screen, 10, 320, 240, 40, theta)
	
def drawBranch(screen, depth, originX, originY, length, theta):
	destinationX = originX + length * math.cos(theta)
	destinationY = originY + length * math.sin(theta)
	color = pygame.Color('green')
	color.g = (int)((float(depth) / 10) * 255);
	pygame.draw.line(screen, color, (originX, originY), (destinationX, destinationY))
	
	thetaOffset = 3.141592 / 4.0;#2.0 * (float(depth) / 10) + 0.1;
	
	if depth > 1:
		drawBranch(screen, depth - 1, destinationX, destinationY, length * 0.95, theta + thetaOffset)
		drawBranch(screen, depth - 1, destinationX, destinationY, length * 0.95, theta - thetaOffset)
		
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