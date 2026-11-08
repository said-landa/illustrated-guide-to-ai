#make a perceptron!

inputs = [
    [ 1,  1,   1, -1],
    [-1,  1,  -1, -1 ],
    [-1,  1,  -1, -1 ],
    [-1,  1,  -1, -1 ]
]

target = 1

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

learningRate = 1
step = target * learningRate if target * output <= 0 else 0
print(step)

if output > 0: print('Positive')
if output < 0: print('Negative')
if output == 0: print(0)
