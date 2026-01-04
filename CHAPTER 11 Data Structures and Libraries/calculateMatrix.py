import numpy as np
def create_matrix():
    newlst = []
    i = 1
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    arr = np.empty((rows,columns))
    for element in arr:
        lst = []
        row = input(f"Enter the numbers for row {i}: ").split(" ")
        for number in row:
            lst.append(int(number))
        newlst.append(lst)
        i = i + 1
    newarr = np.array(newlst)
    return newarr
print("Matrix A:")
matrixA = create_matrix()
print("Matrix B:")
matrixB = create_matrix()
spA = matrixA.shape
spB = matrixB.shape

if spA[0]!= spA[1] and spB[0] != spB[1]:
    print("Both matrices A and B are not square and cannot be inverted.")
elif spA[0]!= spA[1]:
    print("Matrix A is not square and cannot be inverted.")
elif spB[0] != spB[1]:
    print("Matrix B is not square and cannot be inverted.")
else:
    A_inv = np.linalg.inv(matrixA)
    B_inv = np.linalg.inv(matrixB)
    final_result = np.dot(A_inv, B_inv)
    print("Inverse of matrix A:")
    print(A_inv)
    print("Inverse of matrix B:")
    print(B_inv)
    print("Product of A_inv and B_inv:")
    print(final_result)
    
