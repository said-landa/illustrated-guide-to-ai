import numpy as np #does the math
import matplotlib.pyplot as plt #let's us see the letters

examples = np.array( #code the examples manually
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

fig = plt.figure(0, (6,6)) # creates figure number 0 with a size of 6 by 6 inches
for i in range(len(examples)): #loops through the 4 examples
    fig.add_subplot(2, 2, i + 1) #selects a panel ina 2-row, 2-column layout. Matplotlib numbers the panels starting at 1, so i + 1 converts the python index to the panel number.
    plt.imshow(examples[i]) #draws that example in the selected panel, turning each +1 or -1 into a coloured square.