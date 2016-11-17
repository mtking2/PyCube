# PyCube

PyCube is an 3D interactive Rubik's Cube using OpenGL and Pygame.

Here's a .gif showing the progress as of 11/16/16.

<img src="resources/pycube_cpcs.gif" width="500">

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

### TODO

* ~~Individual pieces~~
* ~~Rotation Matrices~~
* ~~90 degree rotation of individual pieces on each axis~~
* ~~Map CW and CWW rotation to lower/upper case keys~~
* ~~Implement all center pieces~~
* ~~Map keys and rotation matrix calls to respective center pieces~~
* ~~Color center pieces~~
* ~~Implement edge pieces~~
* Implement corner pieces
* ~~Solve correct movement of edge pieces~~
    * ~~Use face patterns to track position of edge/corner pieces~~ FAILURE
* ~~Solve correct movement of corner pieces~~
* Color edge pieces
* Color corner pieces
* Test/bug fix function cube
* Test solves with PyCube
* Begin implementing reverse moves solver
* ...

### Notable Mentions

This post from stackoverflow was very helpful in creating a solid starting point
to use quaternions to rotate a 3 dimensional cube using Python and OpenGL.
http://stackoverflow.com/questions/30745703/rotating-a-cube-using-quaternions-in-pyopengl
