__author__ = 'mazurdm1'
import card

class Hand():
    def __init__(self):
        self.currentCards = []

    def gethandtotal(self):
        total = 0
        x = 0
        aces = 0
        for x in range(0, self.currentCards):
            if self.currentCards[x] == 1:
                total += 1

            if self.currentCards[x] == 2:
                total += 2

            if self.currentCards[x] == 3:
                total += 3

            if self.currentCards[x] == 4:
                total += 4

            if self.currentCards[x] == 5:
                total += 5

            if self.currentCards[x] == 6:
                total += 6

            if self.currentCards[x] == 7:
                total += 7

            if self.currentCards[x] == 8:
                total += 8

            if self.currentCards[x] == 9:
                total += 9

            if self.currentCards[x] == 10:
                total += 10

            if self.currentCards[x] == 11:
                total += 10

            if self.currentCards[x] == 12:
                total += 10

            if self.currentCards[x] == 13:
                total += 10

            if self.currentCards[x] == 14:
                aces += 1

        # Deal with any aces, trying to not go over 21.
        while aces > 0:
            if aces < 0:
                if (total > 11) & (aces > 2):
                    total += 11
                else:
                    total += 1
                    aces -= 1

        return total

    def addcard(self, cardvalue):
        self.currentCards.append(cardvalue)

    def show_cards(self):
        cardstring = ""
        for i in self.currentCards:
             if self.currentCards[i] == 1:
                 cardstring += " 1 "

             if self.currentCards[i] == 2:
                 cardstring += " 2 "

             if self.currentCards[i] == 3:
                 cardstring += " 3 "

             if self.currentCards[i] == 4:
                 cardstring += " 4 "

             if self.currentCards[i] == 5:
                 cardstring += " 5 "

             if self.currentCards[i] == 6:
                 cardstring += " 6 "

             if self.currentCards[i] == 7:
                 cardstring += " 7 "

             if self.currentCards[i] == 8:
                 cardstring += " 8 "

             if self.currentCards[i] == 9:
                 cardstring += " 9 "

             if self.currentCards[i] == 10:
                 cardstring += " 10 "

             if self.currentCards[i] == 11:
                 cardstring += " J "

             if self.currentCards[i] == 12:
                 cardstring += " Q "

             if self.currentCards[i] == 13:
                 cardstring += " K "

             if self.currentCards[i] == 14:
                 cardstring += " A "