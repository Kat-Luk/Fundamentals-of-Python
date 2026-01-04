def input_num():
    x = int(input("How many numbers that you want to input:\n"))
    tries = x
    result = 0
    while x != 0:
        try:
            number = float(input(f"{x} number(s) left to input. Enter a number:\n"))
            x = x-1
            result = result + number
        except ValueError:
            print("Wrong input. The input should be a number only.")
    result = round(result, 2)
    return f"The sum of {tries} input numbers is {result}"
print(input_num())

