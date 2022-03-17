import copy
from utilities import *


def find_all_subset(lst):
    list = copy.copy(lst)
    subset = []
    subsets = []

    def actual_function(list, subset):
        for i in range(0, len(list)):
            new_subset = copy.copy(subset)
            new_subset.append(list.pop(0))
            subsets.append(new_subset)
            remain_list = copy.copy(list)
            
            actual_function(remain_list, new_subset)

    actual_function(list, subset)
    return subsets


@get_time
def first_iteration(list):  # O(2^n); ~3s

    data = find_all_subset(list)
    valid = []
    for subset in data:
        temp = calc_profit_and_cost_of_combination(subset)
        profit = temp[1]
        cost = temp[0]
        if cost <= 500:
            valid.append([subset, cost, profit])
    valid.sort(key=lambda x: x[2], reverse=True)
    return(valid[0])
