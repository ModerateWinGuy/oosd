__author__ = 'mazurdm1'
import random
class Deck():

    def __init__(self):
        self.deckcards = []
        i = 0
        for i in range(0, 13):
            x = 0
            for x in range(0, 3):
                self.deckcards.append(i)

    def deal_card(self):
        cardtopull = random.random() * self.deckcards
        card = self.deckcards[cardtopull]
        self.deckcards.remove(self.deckcards, card)
        return card
