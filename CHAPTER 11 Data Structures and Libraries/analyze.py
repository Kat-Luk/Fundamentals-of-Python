import numpy as np
def analyze_nums(lst):
    LIST = []
    for number in lst:
        LIST.append(float(number))
    tupled = tuple(LIST)
    MIN = min(tupled)
    MAX = max(tupled)
    count = len(tupled)
    seted = set(LIST)
    unique = tuple(sorted(seted))
    rever = tupled[::-1]
    m = np.mean(LIST)
    mean = round(m,2)
    return_dict = {
        #"The input list is" : lst,
        "min" : MIN,
        "max" : MAX,
        "count" : count,
        "unique" : unique,
        "reversed" : rever,
        "mean" : mean
        }
    return return_dict

#lst =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '1', '3', '4', '5']
#print(analyze_nums(lst))
