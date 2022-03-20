import numpy as np
from brute_force import *
from action import *
from optimized_KS import *
from optimized_greedy import *
from csv_data import *
from utilities import print_result

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
    [20, 114, 18],
]

# !brute force  (~3s)
# print(first_iteration(raw))

#! optimised knapsack  (~17s)

data_raw = import_data_from_csv("dataset2.csv")
ActionSet.convert_raw_data_to_cent(data_raw)
data = ActionSet(data_raw)
data.instanciate()
result = knapsack(data.actions_obj, 50000)
result["wallet"].sort(key=lambda x: x.profit_per_cent, reverse=True)
print_result(result, True)

#!  optimised gready  (~1e-5s)
# data_raw = import_data_from_csv('dataset2.csv')
# data = ActionSet(data_raw)
# data.instanciate()
# print_result(greedy(data.actions_obj,500))
