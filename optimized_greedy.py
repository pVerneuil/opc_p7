from utilities import get_time


@get_time
def greedy(actions, max_cost):
    actions.sort(key=lambda x: x.profit_per_cent, reverse=True)
    wallet = []
    profit = 0
    cost = 0
    for action in actions:
        if action.price + cost > max_cost:
            continue
        if action.price + cost == max_cost:
            wallet.append(action)
            profit += action.profit
            cost += action.price
            break
        else:
            wallet.append(action)
            profit += action.profit
            cost += action.price
    return {"wallet": wallet, "profit": profit, "cost": cost}
