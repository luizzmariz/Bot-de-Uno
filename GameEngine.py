import UnoCard


class Uno:
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        self.discard_pile = []
        self.current_player_index = 0
        self.direction = 1  # 1 for clockwise, -1 for counter-clockwise

    def deal_cards(self, num_cards=7):
        for player in self.players:
            for _ in range(num_cards):
                card = self.deck.draw_card()
                if card:
                    player.hand.append(card)
    
    def start_game(self):
        # Shuffle the deck
        self.deck.shuffled_deck()
        
        # Deal initial cards to players
        self.deal_cards()

        # Draw the first card for the discard pile
        while True:
            top_card = self.deck.draw_card()
            if top_card and top_card.color is not None:
                self.discard_pile.append(top_card)
                break
            elif top_card:
                self.deck.deck.append(top_card)
        print(f"Starting discard pile: {self.discard_pile[-1]}")

    def next_player(self):
        self.current_player_index = (self.current_player_index + self.direction) % len(self.players)
        return self.players[self.current_player_index]
    
    def newDeckFromDiscardPile(self):
        top_card = self.discard_pile.pop()
        self.deck += self.discard_pile
        self.discard_pile = [top_card]
        self.deck.shuffled_deck()
        print("Deck has been replenished from the discard pile.")
    
    def game(self):

        while(True):
            player = self.players[self.current_player_index]
            card_played = None
            print(f"{player.name}'s turn.")
            
            if not player.has_valid_move(self.discard_pile):
                print(f"{player.name} has no valid moves. Drawing a card.")
                if self.deck.isEmpty():
                    self.newDeckFromDiscardPile()
                player.draw_card(self.deck)
                if player.has_valid_move(self.discard_pile):
                    card_played = player.play_card(self.discard_pile)
                    print(f"{player.name} played {card_played}.")
                else:
                    print(f"{player.name} cannot play the drawn card.")
            else:
                card_played = player.play_card(self.discard_pile)
                print(f"{player.name} played {card_played}.")
            
            if player.has_won():
                print(f"{player.name} has won the game!")
                break

            if card_played in UnoCard.numbers[:10]:
                print(f"{player.name} played a action card: {card_played}.")
                # Here you would implement logic of the action card 
            elif card_played in UnoCard.wild_cards:
                print(f"{player.name} played a wild card: {card_played}.")
                if card_played == 'Wild Draw Four':
                    if not self.deck.hasCards(4):
                        print("Not enough cards in the deck to draw 4. Replenishing from discard pile.")
                        self.newDeckFromDiscardPile()

                    next_player = self.next_player()
                    next_player.draw_card(self.deck, 4)
                    print(f"{next_player.name} drew 4 cards due to Wild Draw Four.")
                print(f"{player.name} chooses the next color.")
                # Here you would implement logic to change the color  
                continue   

            self.next_player()

   