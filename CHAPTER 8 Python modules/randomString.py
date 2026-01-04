# Write a program that uses random module to generate a string contains random characters. Store the value of that string to a variable called str_result. The program should first ask the user how many lowercase characters (stored to low_ch), uppercase characters (stored to up_ch), and digit characters (stored to di_ch) that they want to have in the str_result.

# Example output:

# Enter a number of lowercase characters:
# 5
# Enter a number of uppercase characters:
# 3
# Enter a number of digit characters:
# 4
# Your random string is aG3rHsP8u5i9
import random
low_ch = int(input("Enter a number of lowercase characters: "))
up_ch = int(input("Enter a number of uppercase characters: "))
di_ch = int(input("Enter a number of digit characters: "))
lalphabet = "abcdefghijklmnopqrstvxyz"
ualpahbet = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
numbers = "1234567890"
list_result=[]
for l in range(low_ch):
    list_result.append(random.choice(lalphabet))
for u in range(up_ch):
    list_result.append(random.choice(ualpahbet))
for d in range(di_ch):
    list_result.append(random.choice(numbers))
random.shuffle(list_result)
str_result=""
for character in list_result:
    str_result=str_result+character
print(str_result)

