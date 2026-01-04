def extract_symmetric(lst):
    newlst = []
    for item in lst:
        if item[0] < item[1]:
            a = item[0]
            b = item[1]
            for num in lst:
                if num[0] == b and num[1] == a:
                    newlst.append(item)
    st = set(newlst)
    return st


#lst = [ ( 7, 6 ), ( 8, 9 ), ( 6, 7 ), ( 6, 7 ), ( 2, 3 ), ( 9, 8 ), ( 10, 2 ), ( 2, 10 ), ( 2, 11 ), ( 11, 2 ) ]
#print(extract_symmetric(lst))
