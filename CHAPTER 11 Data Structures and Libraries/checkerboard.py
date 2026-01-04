import numpy as np
def checkerboard(n):
    board = []
    i = 0
    for r in range(n):
        for r in range(n):
            if i % 2 == 0:
                board.append(0)
            else: board.append(1)
            i = i + 1
    arr = np.array(board)
    newarr = arr.reshape(n,n)
    return newarr

#print(checkerboard(5))
            
