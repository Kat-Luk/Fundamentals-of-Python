def sum_nums(lst):
    n = 0
    result = 0
    numbers = []
    while n != len(lst):
        for item in lst:
            try:
                numbers.append(float(item))
                n = n + 1
            except:
                n = n + 1
    for number in numbers:
        result = number + result
    return result
        
#lst = [1,"n",3,"1"]
#print(sum_nums(lst))
