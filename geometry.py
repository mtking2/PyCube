
from OpenGL.GL import *
import time
axis_verts = (
    (-7.5, 0.0, 0.0),
    (7.5, 0.0, 0.0),
    (0.0, -7.5, 0.0),
    (0.0, 7.5, 0.0),
    (0.0, 0.0, -7.5),
    (0.0, 0.0, 7.5)
)

axes = (
    (0, 1),
    (2, 3),
    (4, 5)
)

axis_colors = (
    (1.0, 0.0, 0.0),  # Red
    (0.0, 1.0, 0.0),  # Green
    (0.0, 0.0, 1.0)  # Blue
)

'''
       5____________6
       /           /|
      /           / |
    1/__________2/  |
    |           |   |
    |           |   |
    |           |   7
    |           |  /
    |           | /
    0___________3/
'''

cube_verts = (
    (-3.0, -3.0, 3.0),      # 0
    (-3.0, 3.0, 3.0),       # 1
    (3.0, 3.0, 3.0),        # 2
    (3.0, -3.0, 3.0),       # 3
    (-3.0, -3.0, -3.0),     # 4
    (-3.0, 3.0, -3.0),      # 5
    (3.0, 3.0, -3.0),       # 6
    (3.0, -3.0, -3.0)       # 7
)

cube_stickers = (
    # 0 0
    (-2.95, 1.025, 3.01),
    (-2.95, 2.95, 3.01),
    (-1.025, 2.95, 3.01),
    (-1.025, 1.025, 3.01),

    # 0 1
    (-0.9625, 1.025, 3.01),
    (-0.9625, 2.95, 3.01),
    (0.9625, 2.95, 3.01),
    (0.9625, 1.025, 3.01),

    # 0 2
    (1.025, 1.025, 3.01),
    (1.025, 2.95, 3.01),
    (2.95, 2.95, 3.01),
    (2.95, 1.025, 3.01),

    # 1 0
    (-2.95, -0.9625, 3.01),
    (-2.95, 0.9625, 3.01),
    (-1.025, 0.9625, 3.01),
    (-1.025, -0.9625, 3.01),

    # 1 1
    (-0.9625, -0.9625, 3.01),
    (-0.9625, 0.9625, 3.01),
    (0.9625, 0.9625, 3.01),
    (0.9625, -0.9625, 3.01),

    # 1 2
    (1.025, -0.9625, 3.01),
    (1.025, 0.9625, 3.01),
    (2.95, 0.9625, 3.01),
    (2.95, -0.9625, 3.01),

    # 2 0
    (-2.95, -2.95, 3.01),
    (-2.95, -1.025, 3.01),
    (-1.025, -1.025, 3.01),
    (-1.025, -2.95, 3.01),

    # 2 1
    (-0.9625, -2.95, 3.01),
    (-0.9625, -1.025, 3.01),
    (0.9625, -1.025, 3.01),
    (0.9625, -2.95, 3.01),

    # 2 2
    (1.025, -2.95, 3.01),
    (1.025, -1.025, 3.01),
    (2.95, -1.025, 3.01),
    (2.95, -2.95, 3.01)
)

cube_pieces = (
    (-2.95, -2.95, 2.95),
    (-2.95, -1.025, 2.95),
    (-1.025, -1.025, 2.95),
    (-1.025, -2.95, 2.95),
    (-2.95, -2.95, 1.025),
    (-2.95, -1.025, 1.025),
    (-1.025, -1.025, 1.025),
    (-1.025, -2.95, 1.025)
)

cube_edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 6),
    (5, 1),
    (5, 4),
    (5, 6),
    (7, 3),
    (7, 4),
    (7, 6)
)

up_face = (

    (-3.0, 1.0, 3.0),
    (-3.0, 3.0, 3.0),       # 1
    (3.0, 3.0, 3.0),        # 2
    (3.0, 1.0, 3.0),
    (-3.0, 1.0, -3.0),
    (-3.0, 3.0, -3.0),      # 5
    (3.0, 3.0, -3.0),        # 6
    (3.0, 1.0, -3.0)

    # (0, 1, 2, 3),  # Front
    # (3, 2, 6, 7),  # Right
    # (7, 6, 5, 4),  # Back
    # (4, 5, 1, 0),  # Left
    # (1, 5, 6, 2),  # Top
    # (4, 0, 3, 7)  # Bottom
)

cube_surfaces = (
    [0, 1, 2, 3],  # Front
    [3, 2, 6, 7],  # Right
    [7, 6, 5, 4],  # Back
    [4, 5, 1, 0],  # Left
    [1, 5, 6, 2],  # Top
    [4, 0, 3, 7]  # Bottom
)

cube_colors = (
    (1.0, 1.0, 1.0),  # White
    (0.769, 0.118, 0.227),  # Red
    (1.0, 0.835, 0.0),  # Yellow
    (1.0, 0.345, 0.0),  # Orange
    (0.0, 0.318, 0.729),  # Blue
    (0.0, 0.62, 0.376)  # Green
)


def rotate_y_cw():
    # trans = [1.0, 1.0, -1.0]
    # print(cube_pieces*trans)
    glRotated(time.time() % (1.0) / 1 * -360, 1, 0, 0)
    glColor3f(0.5, 0.5, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()


def axis():
    glBegin(GL_LINES)
    for color, axis in zip(axis_colors, axes):
        glColor3fv(color)
        for point in axis:
            glVertex3fv(axis_verts[point])
    glEnd()


def draw_stickers():
    glBegin(GL_QUADS)
    for v in range(len(cube_stickers)):
        glVertex3fv(cube_stickers[v])
    glEnd()


def drawFace():

    glBegin(GL_LINES)
    glColor3fv((0.5, 0.5, 0.5))
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(up_face[vertex])

    glEnd()


def cube():
    # glBegin(GL_QUADS)
    # for color, surface in zip(cube_colors, cube_surfaces):
    #     glColor3fv(color)
    #     for vertex in surface:
    #         glVertex3fv(cube_verts[vertex])
    # glEnd()

    glBegin(GL_QUADS)
    for surface in cube_surfaces:
        glColor3fv((0.3, 0.3, 0.3))
        for vertex in surface:
            glVertex3fv(cube_verts[vertex])
    glEnd()
    #

    # White
    glColor3fv((1.0, 1.0, 1.0))
    draw_stickers()
    glRotate(90, 1, 0, 0)
    # Blue
    glColor3fv((0.0, 0.318, 0.729))
    draw_stickers()
    glRotate(90, 1, 0, 0)
    # Yellow
    glColor3fv((1.0, 0.835, 0.0))
    draw_stickers()
    glRotate(90, 1, 0, 0)
    # Green
    glColor3fv((0.0, 0.62, 0.376))
    draw_stickers()
    glRotate(90, 0, 1, 0)
    # Orange
    glColor3fv((1.0, 0.345, 0.0))
    draw_stickers()
    glRotate(180, 0, 1, 0)
    # Red
    glColor3fv((0.8, 0.118, 0.118))
    draw_stickers()
    glBegin(GL_LINES)
    glColor3fv((0.5, 0.5, 0.5))
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_verts[vertex])
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_pieces[vertex])
    # for edge in cube_edges:
    #     for vertex in edge:
    #         glVertex3fv(up_face[vertex])
    glEnd()
