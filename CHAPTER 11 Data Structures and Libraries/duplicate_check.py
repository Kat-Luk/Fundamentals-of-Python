def contains_duplicates(lst):
    thisset = set()
    for item in lst:
        thisset.add(item)
    if len(thisset) == len(lst):
        return False
    else:
        return True

#lst = [1,2,3]
#print(contains_duplicates(lst))
