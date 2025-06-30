"""
Here is a template program to work with.
You have been given a function that generates a deck of cards and returns it as a list

1. Write a program that "deals" 6 cards to a player.
2. Print the number of cards in the deck before dealing cards and after dealing cards.

TIP
- Use the player_hand variable to store the cards
- Use the pop() function to "deal" the cards to Player
"""

suits = ["Hearts","Spades","Clubs","Diamonds"]
faces = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
player_hand = []

def build_deck(s,f):
  deck = []
  for suit in s:
    for face in f:
      deck.append(f"{face}:{suit")
  return deck

new_deck = build_deck(suits,faces)
