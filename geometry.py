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

def padding(pad_val):
    for vertex in center_pieces[0]:
        vertex[2]+=pad_val
    for vertex in center_pieces[1]:
        vertex[0]-=pad_val
    for vertex in center_pieces[2]:
        vertex[2]-=pad_val
    for vertex in center_pieces[3]:
        vertex[0]+=pad_val
    for vertex in center_pieces[4]:
        vertex[1]+=pad_val
    for vertex in center_pieces[5]:
        vertex[1]-=pad_val

    for vertex in edge_pieces[0][0]:
        vertex[1]-=pad_val
        vertex[2]+=pad_val
    for vertex in edge_pieces[0][1]:
        vertex[1]+=pad_val
        vertex[2]+=pad_val
    for vertex in edge_pieces[0][2]:
        vertex[1]+=pad_val
        vertex[2]-=pad_val
    for vertex in edge_pieces[0][3]:
        vertex[1]-=pad_val
        vertex[2]-=pad_val

    for vertex in edge_pieces[1][0]:
        vertex[0]-=pad_val
        vertex[2]+=pad_val
    for vertex in edge_pieces[1][1]:
        vertex[0]-=pad_val
        vertex[2]-=pad_val
    for vertex in edge_pieces[1][2]:
        vertex[0]+=pad_val
        vertex[2]-=pad_val
    for vertex in edge_pieces[1][3]:
        vertex[0]+=pad_val
        vertex[2]+=pad_val

    for vertex in edge_pieces[2][0]:
        vertex[0]-=pad_val
        vertex[1]-=pad_val
    for vertex in edge_pieces[2][1]:
        vertex[0]-=pad_val
        vertex[1]+=pad_val
    for vertex in edge_pieces[2][2]:
        vertex[0]+=pad_val
        vertex[1]+=pad_val
    for vertex in edge_pieces[2][3]:
        vertex[0]+=pad_val
        vertex[1]-=pad_val

    for vertex in corner_pieces[0]:
        vertex[0]-=pad_val
        vertex[1]-=pad_val
        vertex[2]+=pad_val
    for vertex in corner_pieces[1]:
        vertex[0]-=pad_val
        vertex[1]+=pad_val
        vertex[2]+=pad_val
    for vertex in corner_pieces[2]:
        vertex[0]+=pad_val
        vertex[1]+=pad_val
        vertex[2]+=pad_val
    for vertex in corner_pieces[3]:
        vertex[0]+=pad_val
        vertex[1]-=pad_val
        vertex[2]+=pad_val
    for vertex in corner_pieces[4]:
        vertex[0]-=pad_val
        vertex[1]-=pad_val
        vertex[2]-=pad_val
    for vertex in corner_pieces[5]:
        vertex[0]-=pad_val
        vertex[1]+=pad_val
        vertex[2]-=pad_val
    for vertex in corner_pieces[6]:
        vertex[0]+=pad_val
        vertex[1]+=pad_val
        vertex[2]-=pad_val
    for vertex in corner_pieces[7]:
        vertex[0]+=pad_val
        vertex[1]-=pad_val
        vertex[2]-=pad_val

center_pieces = [
    # Front 0
    [[-1, -1, 3],
     [-1, 1, 3],
     [1, 1, 3],
     [1, -1, 3],
     [-1, -1, 1],
     [-1, 1, 1],
     [1, 1, 1],
     [1, -1, 1]],

    # Left 1
    [[-3, -1, 1],
     [-3, 1, 1],
     [-1, 1, 1],
     [-1, -1, 1],
     [-3, -1, -1],
     [-3, 1, -1],
     [-1, 1, -1],
     [-1, -1, -1]],

    # Back 2
    [[-1, -1, -1],
     [-1, 1, -1],
     [1, 1, -1],
     [1, -1, -1],
     [-1, -1, -3],
     [-1, 1, -3],
     [1, 1, -3],
     [1, -1, -3],
     ],

    # Right 3
    [[1, -1, 1],
     [1, 1, 1],
     [3, 1, 1],
     [3, -1, 1],
     [1, -1, -1],
     [1, 1, -1],
     [3, 1, -1],
     [3, -1, -1],

     ],

    # Up 3
    [[-1, 1, 1],
     [-1, 3, 1],
     [1, 3, 1],
     [1, 1, 1],
     [-1, 1, -1],
     [-1, 3, -1],
     [1, 3, -1],
     [1, 1, -1]],

    # Down 4
    [[-1, -3, 1],
     [-1, -1, 1],
     [1, -1, 1],
     [1, -3, 1],
     [-1, -3, -1],
     [-1, -1, -1],
     [1, -1, -1],
     [1, -3, -1]]
]

edge_pieces = [
    # X
    # 0
    [[[-1, -3, 3],
      [-1, -1, 3],
      [1, -1, 3],
      [1, -3, 3],
      [-1, -3, 1],
      [-1, -1, 1],
      [1, -1, 1],
      [1, -3, 1]],

     # 1
     [[-1, 1, 3],
      [-1, 3, 3],
      [1, 3, 3],
      [1, 1, 3],
      [-1, 1, 1],
      [-1, 3, 1],
      [1, 3, 1],
      [1, 1, 1]],

     # 2
     [[-1, 1, -1],
      [-1, 3, -1],
      [1, 3, -1],
      [1, 1, -1],
      [-1, 1, -3],
      [-1, 3, -3],
      [1, 3, -3],
      [1, 1, -3]],

     # 3
     [[-1, -3, -1],
      [-1, -1, -1],
      [1, -1, -1],
      [1, -3, -1],
      [-1, -3, -3],
      [-1, -1, -3],
      [1, -1, -3],
      [1, -3, -3]]],

    # Y
    # 0
    [[[-3, -1, 3],
      [-3, 1, 3],
      [-1, 1, 3],
      [-1, -1, 3],
      [-3, -1, 1],
      [-3, 1, 1],
      [-1, 1, 1],
      [-1, -1, 1]],

     # 1
     [[-3, -1, -1],
      [-3, 1, -1],
      [-1, 1, -1],
      [-1, -1, -1],
      [-3, -1, -3],
      [-3, 1, -3],
      [-1, 1, -3],
      [-1, -1, -3]],

     # 2
     [[1, -1, -1],
      [1, 1, -1],
      [3, 1, -1],
      [3, -1, -1],
      [1, -1, -3],
      [1, 1, -3],
      [3, 1, -3],
      [3, -1, -3]],

     # 3
     [[1, -1, 3],
      [1, 1, 3],
      [3, 1, 3],
      [3, -1, 3],
      [1, -1, 1],
      [1, 1, 1],
      [3, 1, 1],
      [3, -1, 1]]],

    # Z
    # 0
    [[[-3, -3, 1],
      [-3, -1, 1],
      [-1, -1, 1],
      [-1, -3, 1],
      [-3, -3, -1],
      [-3, -1, -1],
      [-1, -1, -1],
      [-1, -3, -1]],

     # 1
     [[-3, 1, 1],
      [-3, 3, 1],
      [-1, 3, 1],
      [-1, 1, 1],
      [-3, 1, -1],
      [-3, 3, -1],
      [-1, 3, -1],
      [-1, 1, -1]],

     # 2
     [[1, 1, 1],
      [1, 3, 1],
      [3, 3, 1],
      [3, 1, 1],
      [1, 1, -1],
      [1, 3, -1],
      [3, 3, -1],
      [3, 1, -1]],

     # 3
     [[1, -3, 1],
      [1, -1, 1],
      [3, -1, 1],
      [3, -3, 1],
      [1, -3, -1],
      [1, -1, -1],
      [3, -1, -1],
      [3, -3, -1]]],

]

corner_pieces = [
    # Front
    # 0
    [[-3, -3, 3],
     [-3, -1, 3],
     [-1, -1, 3],
     [-1, -3, 3],
     [-3, -3, 1],
     [-3, -1, 1],
     [-1, -1, 1],
     [-1, -3, 1]],
    # 1
    [[-3, 1, 3],
     [-3, 3, 3],
     [-1, 3, 3],
     [-1, 1, 3],
     [-3, 1, 1],
     [-3, 3, 1],
     [-1, 3, 1],
     [-1, 1, 1]],
    # 2
    [[1, 1, 3],
     [1, 3, 3],
     [3, 3, 3],
     [3, 1, 3],
     [1, 1, 1],
     [1, 3, 1],
     [3, 3, 1],
     [3, 1, 1]],
    # 3
    [[1, -3, 3],
     [1, -1, 3],
     [3, -1, 3],
     [3, -3, 3],
     [1, -3, 1],
     [1, -1, 1],
     [3, -1, 1],
     [3, -3, 1]],

    # Back
    # 0
    [[-3, -3, -1],
     [-3, -1, -1],
     [-1, -1, -1],
     [-1, -3, -1],
     [-3, -3, -3],
     [-3, -1, -3],
     [-1, -1, -3],
     [-1, -3, -3]],
    # 1
    [[-3, 1, -1],
     [-3, 3, -1],
     [-1, 3, -1],
     [-1, 1, -1],
     [-3, 1, -3],
     [-3, 3, -3],
     [-1, 3, -3],
     [-1, 1, -3]],
    # 2
    [[1, 1, -1],
     [1, 3, -1],
     [3, 3, -1],
     [3, 1, -1],
     [1, 1, -3],
     [1, 3, -3],
     [3, 3, -3],
     [3, 1, -3]],
    # 3
    [[1, -3, -1],
     [1, -1, -1],
     [3, -1, -1],
     [3, -3, -1],
     [1, -3, -3],
     [1, -1, -3],
     [3, -1, -3],
     [3, -3, -3]],
]

# [axis, index]
front_edges = [
    [0, 0],  # x
    [0, 1],
    [1, 0],  # y
    [1, 3]
]

left_edges = [
    [1, 0],  # y
    [1, 1],
    [2, 0],  # z
    [2, 1]
]

back_edges = [
    [0, 2],  # x
    [0, 3],
    [1, 1],  # y
    [1, 2]
]

right_edges = [
    [1, 2],  # y
    [1, 3],
    [2, 2],  # z
    [2, 3]
]

up_edges = [
    [0, 1],  # x
    [0, 2],
    [2, 1],  # z
    [2, 2]
]

down_edges = [
    [0, 0],  # x
    [0, 3],
    [2, 0],  # z
    [2, 3]
]

edges = [front_edges,
         left_edges,
         back_edges,
         right_edges,
         up_edges,
         down_edges]


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
    (-3.0, -3.0, 3.0),  # 0
    (-3.0, 3.0, 3.0),  # 1
    (3.0, 3.0, 3.0),  # 2
    (3.0, -3.0, 3.0),  # 3
    (-3.0, -3.0, -3.0),  # 4
    (-3.0, 3.0, -3.0),  # 5
    (3.0, 3.0, -3.0),  # 6
    (3.0, -3.0, -3.0)  # 7
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

cube_surfaces = (
    [0, 1, 2, 3],  # Front 0
    [4, 5, 1, 0],  # Left 1
    [7, 6, 5, 4],  # Back 2
    [3, 2, 6, 7],  # Right 3
    [1, 5, 6, 2],  # Top 4
    [4, 0, 3, 7]  # Bottom 5
)

cube_colors = [
    (0.0, 0.318, 0.729),  # Blue
    (0.8, 0.118, 0.118),  # Red
    (0.0, 0.7, 0.2),  # Green
    (1.0, 0.345, 0.0),  # Orange
    (1.0, 1.0, 1.0),  # White
    (1.0, 0.85, 0.1)  # Yellow
]

pulse_color = [0.0, 0.0, 0.0]
pulse_val = 0.04

# Original
# cube_colors = [
#     (1.0, 1.0, 1.0),  # White
#     (0.8, 0.118, 0.118),  # Red
#     (1.0, 0.95, 0.0),  # Yellow
#     (1.0, 0.345, 0.0),  # Orange
#     (0.0, 0.62, 0.376),  # Green
#     (0.0, 0.318, 0.729)  # Blue
# ]
