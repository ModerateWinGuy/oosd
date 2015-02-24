__author__ = 'mazurdm1'
import hand

class Player():

    def __init__(self):
        self.hold = False
        self.hand = hand()

    def play_turn(self):

    def set_hold(self):
        self.hold = True

    def hit_me(self, card):
        self.hand.addcard(card)


class House(player.Player):
