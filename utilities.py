import time


def get_time(method):
    def timed(*args, **kwargs):
        start_time = time.time()
        result = method(*args, **kwargs)
        end_time = time.time()
        print(
            f'{method.__name__}() took {end_time - start_time} seconds to execute')
        return result

    return timed


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
