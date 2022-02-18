import copy
# import math

# raw = [[1, 20, 5],
#        [2, 30, 10],
#        [3, 50, 15],
#        [4, 70, 20],
#        [5, 60, 17],
#        [6, 80, 25],
#        [7, 22, 7],
#        [8, 26, 11],
#        [9, 48, 13],
#        [10, 34, 27],
#        [11, 42, 17],
#        [12, 110, 9],
#        [13, 38, 23],
#        [14, 14, 1],
#        [15, 18, 3],
#        [16, 8, 8],
#        [17, 4, 12],
#        [18, 10, 14],
#        [19, 24, 21],
#        [20, 114, 18]]


# spent = 0
# max_spent = 500




test = ["a", "b", "c","d"]

 
def permutation(lst):

    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = [] 
    for i in range(len(lst)):
        remLst = copy.copy(lst)
        m = remLst.pop(i)
        for p in permutation(remLst):
            l.append([m] + p)
    return l


l= permutation(test)
print(l)
