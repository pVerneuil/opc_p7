import numpy as np
from utilities import get_time


@get_time
def knapsack(actions, max_cost):

    matrix = np.zeros((len(actions) + 1, max_cost + 1))

    for i in range(len(actions) + 1):
        for j in range(max_cost + 1):
            if i == 0 or j == 0:
                matrix[i, j] = 0
            elif actions[i - 1].price <= j:
                matrix[i, j] = max(
                    actions[i - 1].profit_rounded
                    + matrix[i - 1, j - int(actions[i - 1].price)],
                    matrix[i - 1, j],
                )
            else:
                matrix[i, j] = matrix[i - 1, j]
    best_profit = matrix[len(actions), max_cost]

    wallet = []
    w = max_cost

    for i in range(len(actions), 0, -1):
        if best_profit <= 0:
            break
        if best_profit == matrix[i - 1, int(w)]:
            continue
        else:
            wallet.append(actions[i - 1])
            best_profit -= actions[i - 1].profit_rounded
            w -= actions[i - 1].price
    return {"profit": matrix[len(actions), max_cost], "wallet": wallet}
