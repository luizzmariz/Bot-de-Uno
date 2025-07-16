class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck, num_cards=1):
        card = None
        for _ in range(num_cards):
            card = deck.draw_card()
            self.hand.append(card)        
        return card

    def play_card(self, discard_pile):
        if not self.hand:
            return None
        
        card = self.hand[0]
        

        # In case the card is a Wild card, choose color 
        if(card.color is None):
            color = self.chooseColor()
            card.color = color

        self.hand.remove(card)
        discard_pile.append(card)
                
        return card

    def has_valid_move(self, discard_pile):
        return any(card.can_play_on(discard_pile[-1]) for card in self.hand)
    
    def has_won(self):
        return len(self.hand) == 0
    
    def chooseColor(self):
        maxAmount = 0
        colorChoosen = None
        colors = {'Red': 0, 'Yellow': 0, 'Green': 0, 'Blue': 0}

        for card in self.hand:
           if(card.color is None):
               continue
           colors[card.color] +=1

        for color in colors:
            if colors[color] > maxAmount:
                maxAmount = colors[color]
                colorChoosen = color

        return colorChoosen