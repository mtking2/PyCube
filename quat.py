from math import *
import numpy


def normalize(v, tolerance=0.00001):
    mag2 = sum(n * n for n in v)
    if abs(mag2 - 1.0) > tolerance:
        mag = sqrt(mag2)
        v = tuple(n / mag for n in v)
    return v


def q_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return w, x, y, z


def q_conjugate(q):
    w, x, y, z = q
    return w, -x, -y, -z


def qv_mult(q1, v1):
    q2 = (0.0,) + v1
    return q_mult(q_mult(q1, q2), q_conjugate(q1))[1:]


def axisangle_to_q(v, theta):
    v = normalize(v)
    x, y, z = v
    theta /= 2
    w = cos(theta)
    x *= sin(theta)
    y *= sin(theta)
    z *= sin(theta)
    return w, x, y, z


def q_to_axisangle(q):
    w, v = q[0], q[1:]
    theta = acos(w) * 2.0
    return normalize(v), theta


def q_to_mat4(q):
    w, x, y, z = q
    return numpy.array(
        [[1 - 2 * y * y - 2 * z * z, 2 * x * y - 2 * z * w, 2 * x * z + 2 * y * w, 0],
         [2 * x * y + 2 * z * w, 1 - 2 * x * x - 2 * z * z, 2 * y * z - 2 * x * w, 0],
         [2 * x * z - 2 * y * w, 2 * y * z + 2 * x * w, 1 - 2 * x * x - 2 * y * y, 0],
         [0, 0, 0, 1]], 'f')


def x_rot(v, theta):
    rx = [[1, 0,            0],
          [0, cos(theta),   -sin(theta)],
          [0, sin(theta),   cos(theta)]]
    return numpy.dot(rx, v).tolist()


def y_rot(v, theta):
    rx = [[cos(theta),  0, sin(theta)],
          [0,           1, 0],
          [-sin(theta), 0, cos(theta)]]
    return numpy.dot(rx, v).tolist()


def z_rot(v, theta):
    rx = [[cos(theta),  -sin(theta),    0],
          [sin(theta),  cos(theta),     0],
          [0,           0,              1]]
    return numpy.dot(rx, v).tolist()