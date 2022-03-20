import numpy as np


class Action:
    def __init__(self, action) -> None:
        self.name = action[0]
        self.price = action[1]
        self.profit_per_cent = action[2]
        self.profit = self.price * self.profit_per_cent / 100
        self.profit_rounded = int(round((self.price * self.profit_per_cent) / 100, 2))


class ActionSet:
    def __init__(self, actions) -> None:
        self.actions = actions

    def instanciate(self):
        self.actions_obj = []
        for action in self.actions:
            self.actions_obj.append(Action(action))

    def convert_raw_data_to_cent(data: list):
        for action in data:
            action[1] = int(action[1] * 100)
