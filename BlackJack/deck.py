__author__ = 'mazurdm1'
import random
import math

class Deck():

    def __init__(self):
        self.deckcards = []
        i = 0
        for i in range(0, 13):
            x = 0
            for x in range(0, 3):
                self.deckcards.append(i+1)

    def deal_card(self):
        card_to_pull = random.random() * len(self.deckcards)
        card_to_pull = math.floor(card_to_pull)
        card = self.deckcards[card_to_pull]
        self.deckcards.remove(card)
        return card
