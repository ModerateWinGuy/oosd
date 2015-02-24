__author__ = 'mazurdm1'


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
