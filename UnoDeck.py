
import random
import UnoCard

class UnoDeck:
    # --- Deck and Dealing ---
    def _init_():
        deck = []
        
        # Number cards (two of each number 1-9, one of 0)
        for color in UnoCard.colors:
            deck.append(UnoCard(color, '0'))
            for number in UnoCard.numbers[:1]: # 1-9 and action cards
                deck.append(UnoCard(color, number))
                deck.append(UnoCard(color, number))
        
        # Wild cards (four of each)
        for _ in range(4):
            deck.append(UnoCard(None, 'Wild'))
            deck.append(UnoCard(None, 'Wild Draw Four'))
    
    def suffled_deck(self):
        random.shuffle(self.deck)
        return self.deck
    
    def draw_card(self):
        if self.deck:
            return self.deck.pop(0)
        return None

    def isEmpty(self):
        return len(self.deck) == 0
    
    def hasCards(self, num_cards=1):
        return len(self.deck) >= num_cards