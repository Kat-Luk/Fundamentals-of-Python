import csv
input_file = input("Enter the file name: ")
file = open(input_file)
reader = csv.DictReader(file)
SUM = 0
index = 0
key = ""
for row in reader:
    for r in row:
        index += 1
        if index == 2:
            key = r   
    SUM = float(row[key]) + SUM
sum_result = round(SUM, 2)
print(f"The sum of all numbers in the second column is: {sum_result}")
