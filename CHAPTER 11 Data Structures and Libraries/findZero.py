import numpy as np
def findZero():
    i = 1
    newlst = []
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    arr = np.empty((rows,columns))
    for element in arr:
        lst = []
        row = input(f"Enter row {i}: ").split(" ")
        for number in row:
            lst.append(int(number))
        newlst.append(lst)
        i = 1+i
    newarr = np.array(newlst)

    index_c= -1
    index_r = -1
    for j in range(rows):
        for i in range(columns):
            if int(newarr[j,i]) == 0:
                index_c = i
                index_r = j
                if index_r != -1:
                    for r in range(rows):
                        newarr[r, index_c] = 0
                if index_c != -1:
                    for c in range(columns):
                        newarr[index_r, c] = 0
                return f"Modified  matrix:\n{newarr}"
    return f"Modified  matrix:\n{newarr}"
            


print(findZero())
