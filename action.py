import numpy as np


class Action:

    def __init__(self, action) -> None:
        self.name = action[0]
        self.price = float(action[1])
        self.profit_per_cent = float(action[2])
        self.profit = (self.price * self.profit_per_cent) / 100


class ActionSet:

    def __init__(self, actions) -> None:
        self.actions = actions

    def instanciate(self):
        self.actions_obj = []
        for action in self.actions:
            self.actions_obj.append(Action(action))
