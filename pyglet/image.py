import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('kitten.jpg')

@window.event
def on_draw():
	window.clear()
	image.blit( (window.width - image.width) // 2, (window.height - image.height) // 2)

pyglet.app.run()
