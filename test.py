import numpy as np
from brute_force import *
from action import *
from optimized import *
from csv_data import *

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

# brute force
# print(first_iteration(raw))

# optimised

ActionSet.convert_raw_data_to_cent(raw)

set_test = ActionSet(raw)

# set_test.instanciate()
# print(knapsack(set_test.actions_obj, 50000))

data_raw = import_data_from_csv('dataset1.csv')
# ActionSet.convert_raw_data_to_cent(data_raw)
data = ActionSet(data_raw)
data.instanciate()
result = knapsack(data.actions_obj, 500)
print(result)

