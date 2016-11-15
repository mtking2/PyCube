# PyCube

PyCube is an 3D interactive Rubik's Cube using OpenGL and Pygame.

### Purpose
This software-based Rubik's Cube will serve as a basis for a later
project in which I will attempt to create another program, implementing
a neural network algorithm, that will teach itself to solve a Rubik's Cube (PyCube).


### Dependencies

This program utilizes the following Python modules:  
[PyOpenGL](pyopengl.sourceforge.net/) see also [OpenGL](https://www.opengl.org/)  
[Pygame](http://pygame.org/)  
[NumPy](http://www.numpy.org/)

Python 3.x :  
`pip3 install pyopengl pygame numpy`

~~Python 2.x :  
`pip install pyopengl pygame numpy`~~  
Only supported by Python 3.x+. Try at your own risk.

### Notable Mentions

This post from stackoverflow was very helpful in creating a solid starting point
to use quaternions to rotate a 3 dimensional cube using Python and OpenGL.
http://stackoverflow.com/questions/30745703/rotating-a-cube-using-quaternions-in-pyopengl
