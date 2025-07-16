from GameEngine import Uno
from Player import Player
from UnoDeck import UnoDeck

strategy1 = ['wild_card_strategy', 'change_color_strategy', 'same_color_strategy']
strategy2 = ['change_color_strategy', 'same_color_strategy','wild_card_strategy']
strategy3 = ['same_color_strategy', 'wild_card_strategy', 'change_color_strategy']

p1 = Player("Player 1", strategy1)
p2 = Player("Player 2", strategy2)
p3 = Player("Player 3", strategy3)
deck = UnoDeck()

uno = Uno([p1,p2, p3], deck)

uno.start_game()
uno.game()