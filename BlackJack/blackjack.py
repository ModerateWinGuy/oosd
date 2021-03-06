import sys
import player
import deck

person_Player = player.Player()
housePlayer = player.House()
card_Deck = deck.Deck()
gameOver = False

print("Time to play Blackjack!")
# Deal 2 cards each cards.
person_Player.hit_me(card_Deck.deal_card())
person_Player.hit_me(card_Deck.deal_card())
housePlayer.hit_me(card_Deck.deal_card())
housePlayer.hit_me(card_Deck.deal_card())

# Display cards, with one dealers card obscured.
print("Player:")
print(person_Player.display_hand())
print("House:")
print(housePlayer.display_hand())
# Player hits until bust, blackjack, or holds.
while person_Player.hold is False and person_Player.bust is False:
    person_Player.play_turn(card_Deck)
    print("Player:")
    print(person_Player.display_hand())
    print("House:")
    print(housePlayer.display_hand())

# House hits until over 16 or bust.
while housePlayer.done is False:
    housePlayer.play_turn()

# Game over
