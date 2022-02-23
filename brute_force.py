import copy
import time

def calc_profit_and_cost_of_combination(combination):
    """calculate profit and costs of a combination of action

    Args:
        combination (list): action in the format [ id , cost, margin]
    Returns:
    [cost, profit]
    """
    cost = 0
    profit = 0
    for action in combination:
        cost += action[1]
        profit += action[1]*action[2]/100
    return[cost, profit]


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

raw = [
    [1, 20, 5],
    [2, 30, 10],
    [3, 50, 15],
    [4, 70, 20],
    [5, 60, 17],
    [6, 80, 25],
    [7, 22, 7],
    [8, 26, 11],
    [9, 48, 13],
    [10, 34, 27],
    [11, 42, 17],
    [12, 110, 9],
    [13, 38, 23],
    [14, 14, 1],
    [15, 18, 3],
    [16, 8, 8],
    [17, 4, 12],
    [18, 10, 14],
    [19, 24, 21],
    [20, 114, 18]]


def first_iteration(list): #O(2^n); ~3s 

    start_time = time.time()

    data = find_all_subset(list)
    valid = []
    for subset in data:
        temp = calc_profit_and_cost_of_combination(subset)
        profit = temp[1]
        cost = temp[0]
        if cost <= 500:
            valid.append([subset, cost,profit])
    valid.sort(key=lambda x: x[2], reverse=True)
    print (len(valid))
    print(valid[0])
    print("--- %s seconds ---" % (time.time() - start_time))

first_iteration(raw)


