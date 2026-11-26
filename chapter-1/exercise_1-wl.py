import numpy as np 
import matplotlib.pyplot as plt

examples = np.array(
    [
        [ 1,  1,  1, -1],
        [-1,  1, -1, -1],
        [-1,  1, -1, -1], #T shifted left
        [-1,  1, -1, -1]
    ], 
    [
        [-1,  1,  1,  1],
        [-1, -1,  1, -1], #T shifted right
        [-1, -1,  1, -1],
        [-1, -1,  1, -1]
    ],
    [
        [-1, -1,  1, -1],
        [-1, -1,  1, -1],
        [ 1, -1,  1, -1], #J shifted left
        [ 1,  1,  1, -1]
    ],
    [
        [-1, -1, -1,  1],
        [-1, -1, -1,  1],
        [-1,  1, -1,  1], #J shifted right
        [-1,  1,  1,  1]
    ]
)