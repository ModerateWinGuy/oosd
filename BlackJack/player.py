import hand


class Player():

    def __init__(self):
        self.hold = False
        self.hand = hand.Hand()

    def set_hold(self):
        self.hold = True

    def play_turn(self):
        if input("(h)it or (s)tand: ") == "h":
            self.hand.addcard()
        else:
            self.set_hold()

    def hit_me(self, card):
        self.hand.addcard(card)

    def display_hand(self):
        return self.hand.show_cards()


class House(Player):

    def play_turn(self):
        temp = ""
        temp = self.hand.show_cards()
