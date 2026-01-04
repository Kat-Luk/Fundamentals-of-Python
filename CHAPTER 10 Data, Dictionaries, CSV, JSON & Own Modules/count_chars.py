def count_chars(s):
    dictionary = {}
    for character in s:
        if character not in dictionary:
            dictionary[character] = 1
        else:
            dictionary[character] =  dictionary[character] + 1
    return dictionary

#string = "This is a test."
#result = count_chars(string)
#print(result)
