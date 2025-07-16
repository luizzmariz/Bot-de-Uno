from GameEngine import Uno
from Player import Player
from UnoDeck import UnoDeck

p1 = Player("Player 1")
p2 = Player("Player 2")
p3 = Player("Player 3")
deck = UnoDeck()

uno = Uno([p1,p2, p3], deck)

uno.start_game()
uno.game()