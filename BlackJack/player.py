import hand
import strategy


class Player():

    def __init__(self):
        self.hold = False
        self.bust = False
        self.hand = hand.Hand()

    def set_hold(self):
        self.hold = True

    def play_turn(self, deck):
        if input("(h)it or (s)tand: ") == "h":
            self.hand.addcard(deck.deal_card())
        else:
            self.set_hold()

    def hit_me(self, card):
        self.hand.addcard(card)

    def display_hand(self):
        return self.hand.show_cards()


class House(Player):

    def __init__(self):
        super.__init__()
        self.strat = strategy.Strategy()
        self.done = False

    def play_turn(self, deck):
        if self.strat.hit() is True:
            self.hand.addcard(deck.deal_card())
        temp = ""
        temp = self.hand.show_cards()
