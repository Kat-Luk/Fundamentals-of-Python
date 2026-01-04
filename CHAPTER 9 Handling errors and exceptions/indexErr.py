try:
    numbers = input("Enter a list, separated by commas: \n").split(",")
    index = int(input(f"There are currently {len(numbers)} items in the list. Enter an index number:\n"))
    print(f"The item in index {index} is {numbers[index]}.")
except IndexError:
    print(f"Error: Out of the list. There are only {len(numbers)} items in the list.")
