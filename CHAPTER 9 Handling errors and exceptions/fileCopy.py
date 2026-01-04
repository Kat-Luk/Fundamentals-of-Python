try:
    source_file = input("Enter the source filename:")
    destination_file = input("Enter the destination filename:")
    file = open(source_file,"r")
    lines = []
    for line in file:
        lines.append(line)
    file.close()
    file = open(destination_file,"w")
    file.close()
    file = open(destination_file,"a")
    for line in lines:
        file.write(line)
    file.close()
    print("File copied successfully.")
except FileNotFoundError:
    print("Error: Source file not found.")
