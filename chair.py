from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from numpy import *


def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    # glOrtho(-10,10,-10,10,-10,10) ##2d##
    gluPerspective(60, 1, 0.1, 50)
    gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)


def draw_chair():
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 1,0)
    glTranslate(0, 0, 0)
    glScale(2, 2, .5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 1 , 0)
    glTranslate(0, -2,2)
    glScale(2, .5, 2)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()


def draw_cube():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    draw_chair()
    glTranslate(5, 0, 0)
    draw_chair()

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Sec6")
glutInitWindowSize(500, 500)
glutDisplayFunc(draw_cube)
glutIdleFunc(draw_cube)
myinit()
glutMainLoop()
