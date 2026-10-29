#make a perceptron!

inputs = [
    [-1, -1,  1, -1 ],
    [-1, -1,  1, -1 ],
    [ 1, -1,  1, -1 ],
    [ 1,  1,  1, -1 ]
]

weights = [
    [2, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, -3]
]

output = 0

for row in range(0, len(inputs)):
    for column in range(0, len(inputs[row])):
        output += inputs[row][column] * weights[row][column]

if output > 0: print(f'{output} T')
if output < 0: print('J')
if output == 0: print(0)
