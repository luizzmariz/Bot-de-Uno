class Player:
    def __init__(self, name, stategies):
        self.name = name
        self.hand = []
        self.stategies = stategies

    def draw_card(self, deck, num_cards=1):
        card = None
        for _ in range(num_cards):
            card = deck.draw_card()
            self.hand.append(card)        
        return card

    def play_card(self, discard_pile):
        if not self.hand:
            return None
        
        # Play card strategy
        for strategy in self.stategies:
            match strategy:
                case 'wild_card_strategy':
                    result = self.wild_card_strategy()
                case 'change_color_strategy':
                    result = self.change_color_strategy(discard_pile[-1])
                case 'same_color_strategy':
                    result = self.same_color_strategy(discard_pile[-1])
            
            # If a strategy returns a card, play it
            if result:
                card = result
                break
        
        # card = self.hand[0]
        

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
    
    def wild_card_strategy(self):
        print(self.name + " is trying wild card strategy")
        if any(card.color is None for card in self.hand):
            # If there is a wild card, play it
            for card in self.hand:
                if card.color is None:
                    return card 
        return None


    def change_color_strategy(self, top_card):
        print(self.name + " is trying change color strategy")
        for card in self.hand:
            # Same value, different color
            if card.color is not None and card.color != top_card.color and card.value == top_card.value:
                return card
        
        return None

    def same_color_strategy(self, top_card):
        print(self.name + " is trying same color strategy")
        for card in self.hand:
            # Same color
            if card.color == top_card.color:
                return card
        
        return None
    