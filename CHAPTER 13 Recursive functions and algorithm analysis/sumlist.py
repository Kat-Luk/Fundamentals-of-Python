def sum_of_list_recursive(numbers):
    if len(numbers) == 0:
        return 0
    else:
        n = int(numbers[0])
        return sum_of_list_recursive(numbers[1:])+n
#lst = [1,2,1,3,0,4]
#print(sum_of_list_recursive(lst))
