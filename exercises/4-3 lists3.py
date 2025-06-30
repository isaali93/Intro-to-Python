"""
Here is a template program to work with.
You have been given a function that generates a deck of cards and returns it as a list

Write a program that "deals" 6 cards to a player.
"""

suits = ["Hearts","Spades","Clubs","Diamonds"]
faces = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

def build_deck(s,f):
  deck = []
  for suit in s:
    for face in f:
      deck.append(f"{face}:{suit")
  return deck

new_deck = build_deck(suits,faces)
