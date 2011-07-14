import pyglet
from pyglet.gl import *

window = pyglet.window.Window()
image = pyglet.resource.image('kitten.jpg')
texture = image.get_texture()

@window.event
def on_draw():
	# set ortho projection
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0, window.width, 0, window.height, -1, 1)
	glTranslatef(0, 0, -0.5)
	
	# set up the camera
	glMatrixMode(GL_MODELVIEW)
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()

	glEnable(texture.target)
	glColor3f(1.0, 1.0, 1.0)
	glBindTexture(texture.target, texture.id)

	print texture.tex_coords

	# draw the image on the screen
	originX = (window.width - image.width) / 2
	originY = (window.height - image.height) / 2
	pyglet.graphics.draw(4, GL_QUADS,
		('v2f', (originX, originY,
			originX + image.width, originY,
			originX + image.width, originY + image.height,
			originX, originY + image.height)),
		('t3f', texture.tex_coords)
	)

pyglet.app.run()
