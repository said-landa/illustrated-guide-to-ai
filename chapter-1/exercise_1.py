#make a perceptron!

t_left = [
    [ 1,  1,   1, -1],
    [-1,  1,  -1, -1 ],
    [-1,  1,  -1, -1 ],
    [-1,  1,  -1, -1 ]
]

t_right = [
    [-1, 1, 1, 1],
    [-1, -1, 1, -1],
    [-1, -1, 1, -1],
    [-1, -1, 1, -1]
]

j_left = [
    [-1, -1, 1, -1],
    [-1, -1, 1, -1],
    [ 1, -1, 1, -1],
    [ 1,  1, 1, -1]
]

j_right = [
    [-1, -1,  -1, 1],
    [-1, -1,  -1, 1],
    [-1,  1,  -1, 1],
    [-1,  1,   1, 1]
]

examples = [(t_left, 1), (t_right, 1), (j_left, -1), (j_right, -1)]

weights = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

#training
for inputs, target in examples:
    output = 0
    for row in range(0, len(inputs)):
        for column in range(0, len(inputs[row])):
            output += inputs[row][column] * weights[row][column]   

    learningRate = 1
    step = target * learningRate if target * output <= 0 else 0

    print(step)

    for row in range(len(inputs)):
        for column in range(len(inputs[row])):
            weights[row][column] += step * inputs[row][column]

#testing
for inputs, target in examples:
    output = 0
    for row in range(len(inputs)):
        for column in range(len(inputs[row])):
            output += inputs[row][column] * weights[row][column]

    if output > 0: print('Positive')
    if output < 0: print('Negative')
    if output == 0: print(0)
    print("Correct: ", target * output > 0)
