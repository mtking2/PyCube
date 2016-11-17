""" PyCube
Author: Michael King

Based and modified from original version found at:
http://stackoverflow.com/questions/30745703/rotating-a-cube-using-quaternions-in-pyopengl
"""

from quat import *
from geometry import *

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


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

'''
    These pattern are for each set of edge pieces and corner
    pieces on each face. They will shift when the faces are
    rotated so these patterns will keep track of them.
     _______________
    |  1 |  2 |  2 |
    |____|____|____|
    | 1  |    |  3 |
    |____|____|____|
    |  0 |  0 |  3 |
    |____|____|____|

'''
# face_patterns = [
#     [0, 1, 2, 3],  # 0 Front
#     [0, 1, 2, 3],  # 1 Back
#     [0, 1, 2, 3],  # 2 Left
#     [0, 1, 2, 3],  # 3 Right
#     [0, 1, 2, 3],  # 4 Up
#     [0, 1, 2, 3],  # 5 Down
# ]
#
# front_edges = [
#     [0, 1],  # x
#     [0, 3]   # y
# ]
#
# back_edges = [
#     [2, 3],  # x
#     [1, 2]   # y
# ]
#
# left_edges = [
#     [0, 1],  # y
#     [0, 1]   # z
# ]
#
# right_edges = [
#     [2, 3],  # y
#     [2, 3]   # z
# ]

def draw_face():

    glBegin(GL_LINES)
    glColor3fv((0.5, 0.5, 0.5))
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(up_face[vertex])

    glEnd()


def draw_stickers():
    glBegin(GL_QUADS)
    for v in range(len(cube_stickers)):
        glVertex3fv(cube_stickers[v])
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


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('PyCube')

    # Using depth test to make sure closer colors are shown over further ones
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    # Default view
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.5, 40)
    glTranslatef(0.0, 0.0, -17.5)

    # set initial rotation
    # glRotate(90, 1, 0, 0)
    # glRotate(-15, 0, 0, 1)
    # glRotate(15, 1, 0, 0)

    inc_x = 0
    inc_y = 0
    accum = (1, 0, 0, 0)
    zoom = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # Rotating about the x axis
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    inc_x = pi / 100
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    inc_x = -pi / 100

                # Rotating about the y axis
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    inc_y = pi / 100
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    inc_y = -pi / 100

                if event.key == pygame.K_u:
                    print('up')

                # Reset to default view
                if event.key == pygame.K_SPACE:
                    inc_x = 0
                    inc_y = 0
                    accum = (1, 0, 0, 0)
                    zoom = 1

            if event.type == pygame.KEYUP:
                # Stoping rotation
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or \
                                event.key == pygame.K_w or event.key == pygame.K_s:
                    inc_x = 0.0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or \
                                event.key == pygame.K_a or event.key == pygame.K_d or \
                                event.key == pygame.K_u:
                    inc_y = 0.0

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Increase scale (zoom) value
                if event.button == 4:
                    if zoom < 1.6:
                        zoom += 0.05
                    # print('scroll up', zoom)
            if event.type == pygame.MOUSEBUTTONUP:
                # Increase scale (zoom) value
                if event.button == 5:
                    if zoom > 0.2:
                        zoom -= 0.05
                    # print('scroll down', zoom)

        # Get relative movement of mouse coordinates and update x and y incs
        if pygame.mouse.get_pressed()[0] == 1:
            (tmp_x, tmp_y) = pygame.mouse.get_rel()
            # print(tmp_x, tmp_y)
            inc_x = -tmp_y * pi / 450
            inc_y = -tmp_x * pi / 450

        pygame.mouse.get_rel()  # prevents the cube from instantly rotating to a newly clicked mouse coordinate

        rot_x = normalize(axisangle_to_q((1.0, 0.0, 0.0), inc_x))
        rot_y = normalize(axisangle_to_q((0.0, 1.0, 0.0), inc_y))

        accum = q_mult(accum, rot_x)
        accum = q_mult(accum, rot_y)

        glMatrixMode(GL_MODELVIEW)
        glLoadMatrixf(q_to_mat4(accum))
        glScalef(zoom, zoom, zoom)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        cube()
        # drawFace()
        # draw_axis()
        pygame.display.flip()
        # pygame.time.wait(1)


main()