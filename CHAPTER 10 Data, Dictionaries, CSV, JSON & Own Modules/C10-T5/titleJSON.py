import json
input_file  = input("Enter the file name: ")
file = open(input_file)
books = json.load(file)
index = 0
titles = []
for row in books:
    for key in row:
        if index % 3 == 0:
            titles.append(row[key])
        index += 1
print("All the title of books in the JSON file:")
for title in titles:
    print("- ",title)
