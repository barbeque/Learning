require "opengl"
require "mathn"

# use the namespaces
include Gl
include Glu
include Glut

window = ""

def initGLWindow(width = 640, height = 480)
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClearDepth(1.0)
	glDepthFunc(GL_LEQUAL)
	glEnable(GL_DEPTH_TEST)
	glShadeModel(GL_SMOOTH)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity
	gluPerspective(45.0, width / height, 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)
	drawGLScene
end

def reshape(width, height)
	height = 1 if height == 0
	
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity
	gluPerspective(45.0, width / height, 0.1, 100.0)
end

def drawGLScene
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity

	glTranslatef(-1.5, 0.0, -6.0)
	
	glBegin(GL_POLYGON)
		glVertex3f(0.0, 1.0, 0.0)
		glVertex3f(1.0, -1.0, 0.0)
		glVertex3f(-1.0, -1.0, 0.0)
	glEnd

	glTranslatef(3.0, 0.0, 0.0)
	glBegin(GL_QUADS)
		glVertex3f(-1.0, 1.0, 0.0)
		glVertex3f(1.0, 1.0, 0.0)
		glVertex3f(1.0, -1.0, 0.0)
		glVertex3f(-1.0, -1.0, 0.0)
	glEnd

	glutSwapBuffers
end

def idle
	glutPostRedisplay
end

keyboard = lambda do | key, x, y |
	case(key)
		when ?\e
			# escape
			glutDestroyWindow(window)
			exit(0)
		end
		glutPostRedisplay
end

glutInit
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(640, 480)
glutInitWindowPosition(0,0)
window = glutCreateWindow("NeHe demo #2 in Ruby!")
glutDisplayFunc(method(:drawGLScene).to_proc)
glutReshapeFunc(method(:reshape).to_proc)
glutIdleFunc(method(:idle).to_proc)
glutKeyboardFunc(keyboard)
initGLWindow(640, 480)
glutMainLoop()
