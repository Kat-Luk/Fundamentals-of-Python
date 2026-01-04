def sort_lst_tup(tup):
    llst = list(tup)
    i = 0
    for lst in tup:
        sorted_lst = sorted(lst)
        llst[i] = sorted_lst
        i = i + 1
    newtup = tuple(llst)
    return newtup
        

#tup = ([5,2,7,1,6,0], [50,10,22,90,12], [500,600,100,550,800,400])
#print(sort_lst_tup(tup))
