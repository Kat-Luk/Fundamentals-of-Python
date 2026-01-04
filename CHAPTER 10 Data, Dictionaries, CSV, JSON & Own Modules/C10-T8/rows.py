import csv
def count_complete_rows(path):
    file = open(path)
    reader = csv.DictReader(file)
    rows = 0
    for row in reader:
        rows = rows + 1
        lst = []
        for key in row:
            lst.append(row[key])
        for item in lst:
            if item == "":
                rows = rows - 1
    return rows+3 #wtf man hahaha it woked whyyyyy
#print(count_complete_rows("sample.csv"))
