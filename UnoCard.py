class UnoCard:
    # --- Card Representation ---
    colors = ['Red', 'Yellow', 'Green', 'Blue']
    numbers = [str(i) for i in range(10)] + ['Skip', 'Reverse', 'Draw Two']
    wild_cards = ['Wild', 'Wild Draw Four']

    def __init__(self, color=None, value=None):
        self.color = color
        self.value = value

    def __str__(self):
        if self.color:
            return f"{self.color} {self.value}"
        else:
            return self.value # For Wild cards

    def __repr__(self):
        return self.__str__()

    def can_play_on(self, top_card):
        if self.color is None: # Wild card
            return True
        if top_card.color is None: # Top card is a Wild card
            return True
        return self.color == top_card.color or self.value == top_card.value
