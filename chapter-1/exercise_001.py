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

output = 0

for row in range(0, len(inputs)):
    for column in range(0, len(inputs[row])):
        output += inputs[row][column] * weights[row][column]

print(output)