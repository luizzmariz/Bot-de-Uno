from UnoCard import UnoCard

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

    def next_player(self):
        self.current_player_index = (self.current_player_index + self.direction) % len(self.players)
        return self.players[self.current_player_index]
    
    def newDeckFromDiscardPile(self):
        top_card = self.discard_pile.pop()
        self.deck.deck += self.discard_pile
        self.discard_pile = [top_card]
        self.deck.shuffle()
        #print("Deck has been replenished from the discard pile.")
    
    
    def prepare_game(self):
        # Shuffle the deck
        self.deck.shuffle()
        
        # Deal initial cards to players
        self.deal_cards()

        # Draw the first card for the discard pile
        while True:
            top_card = self.deck.draw_card()
            if top_card.color is not None:
                self.discard_pile.append(top_card)
                break
            else:
                self.deck.deck.append(top_card)
        print(f"Starting discard pile: {self.discard_pile[-1]}")

    def game(self):
        while(True):
            player = self.players[self.current_player_index]
            card_played = None
            print("--------------------------------------")
            print(f"{player.name}'s turn.")
            print(f"Current Discard Pile Card: {self.discard_pile[-1]}")
            #print(f"{player.name} Current hand: {player.hand}")

            
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
                return self.players.index(player)

            if card_played and card_played.value in UnoCard.numbers[10:]:
                print(f"{player.name} played a action card: {card_played}.")
                match card_played.value:
                    case 'Skip':
                        next_player = self.next_player()
                        print(f"Player {next_player.name} has lost its turn due to Skip.")
                    case 'Reverse':
                        self.direction *= -1
                        print(f"Game direction has changed to {self.direction} due to Reverse")
                    case 'Draw Two':
                        if not self.deck.hasCards(2):
                            print("Not enough cards in the deck to draw 2. Replenishing from discard pile.")
                            self.newDeckFromDiscardPile()

                        next_player = self.next_player()
                        next_player.draw_card(self.deck, 2)
                        print(f"{next_player.name} drew 2 cards due to Draw Two.")
            elif card_played and card_played.value in UnoCard.wild_cards:
                print(f"{player.name} played a wild card: {card_played}.")
                if card_played.value == 'Wild Draw Four':
                    if not self.deck.hasCards(4):
                        print("Not enough cards in the deck to draw 4. Replenishing from discard pile.")
                        self.newDeckFromDiscardPile()

                    next_player = self.next_player()
                    next_player.draw_card(self.deck, 4)
                    print(f"{next_player.name} drew 4 cards due to Wild Draw Four.")
                #print(f"{player.name} choose the next color as {card_played.color}.")

            self.next_player()
        
    def start_game(self):

        self.prepare_game()
        
        return self.game()



   