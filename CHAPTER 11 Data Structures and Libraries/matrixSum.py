import numpy as np
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
arr = np.empty((rows,columns))
newlst = []
i = 1
sum_rows = []
sum_columns = []
total_sum = 0
for element in arr:
    lst = []
    row = input(f"Enter the numbers for row {i}: ").split(" ")
    for number in row:
        total_sum = total_sum + int(number)
        lst.append(int(number))
    newlst.append(lst)
    sum_rows.append(sum(lst))
    i = 1+i
newarr = np.array(newlst)
for i in range(columns):
    SUM = 0
    for j in range(rows):
        SUM = int(newarr[j,i]) + SUM
    sum_columns.append(SUM)

#print(newarr)
print(f"Row sums: {sum_rows}")
print(f"Column sums: {sum_columns}")
print(f"Total sum: {total_sum}")
