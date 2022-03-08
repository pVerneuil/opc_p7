
import numpy as np


class Action:

    def __init__(self, action) -> None:
        self.name = action[0]
        self.price = action[1]
        self.profit_per_cent = action[2]
        self.profit = int(round((self.price * self.profit_per_cent) / 100,1))

    def convert_to_cent(self):
        self.price = self.price*100
        self.profit = self.profit*100

    def convert_to_euro(self):
        self.price = self.price/100
        self.profit = self.profit/100


class ActionSet:

    def __init__(self, actions) -> None:
        self.actions = actions

    def instanciate(self):
        self.actions_obj = []
        for action in self.actions:
            self.actions_obj.append(Action(action))

    def convert_raw_data_to_cent(data:list):
        for action in data:
            action[1]= int(action[1]*100)
 
    def convert_set_to_euro(self):
        for action in self.actions_obj:
            action.convert_to_euro()

    def convert_set_to_cent(self):
        for action in self.actions_obj:
            action.convert_to_cent()