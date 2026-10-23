inputs = [
    [1, 1, 1, -1],
    [-1, 1, -1, -1],
    [-1, 1, -1, -1],
    [-1, 1, -1, -1]
]

weights = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for row in range(0, len(inputs)):
    for column in range(0, len(inputs[row])):
        print(inputs[row][column] * weights[row][column]) 