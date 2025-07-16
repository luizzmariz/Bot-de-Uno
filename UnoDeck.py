
import random

from UnoCard import UnoCard

class UnoDeck:
    deck = []

    # --- Deck and Dealing ---
    def __init__(self):
        print("creating deck")
        # Number cards (two of each number 1-9, one of 0)
        for color in UnoCard.colors:
            self.deck.append(UnoCard(color, '0'))
            for number in UnoCard.numbers[1:]: # 1-9 and action cards
                self.deck.append(UnoCard(color, number))
                self.deck.append(UnoCard(color, number))
        
        # Wild cards (four of each)
        for _ in range(4):
            self.deck.append(UnoCard(None, 'Wild'))
            self.deck.append(UnoCard(None, 'Wild Draw Four'))
        
        print(self.deck)
    
    def shuffled_deck(self):
        random.shuffle(self.deck)
        return self.deck
    
    def draw_card(self):
        return self.deck.pop(0)

    def isEmpty(self):
        return len(self.deck) == 0
    
    def hasCards(self, num_cards=1):
        return len(self.deck) >= num_cards