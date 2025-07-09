class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck, num_cards=1):
        card = None
        for _ in range(num_cards):
            card = deck.pop(0)
            self.hand.append(card)        
        return card

    def play_card(self, discard_pile):
        if not self.hand:
            return None
        
        card = self.hand[0]
        
        self.hand.remove(card)
        discard_pile.append(card)
        return card

    def has_valid_move(self, discard_pile):
        return any(card.can_play_on(discard_pile[-1]) for card in self.hand)
    
    def has_won(self):
        return len(self.hand) == 0