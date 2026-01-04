def sum_of_digits_recursive(n):
    x = str(n)
    if len(x) == 1:
        return int(x)
    else:
        f = x[0]
        return sum_of_digits_recursive(x[1:])+int(f)

#n = 123
#print(sum_of_digits_recursive(n))
