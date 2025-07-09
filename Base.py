# prompt: Create a game of Uno

import random

# --- Card Representation ---
colors = ['Red', 'Yellow', 'Green', 'Blue']
numbers = [str(i) for i in range(10)] + ['Skip', 'Reverse', 'Draw Two']
wild_cards = ['Wild', 'Wild Draw Four']

class UnoCard:
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

# --- Deck and Dealing ---
def create_uno_deck():
    deck = []
    # Number cards (two of each number 1-9, one of 0)
    for color in colors:
        deck.append(UnoCard(color, '0'))
        for number in numbers[:9]: # 1-9
            deck.append(UnoCard(color, number))
            deck.append(UnoCard(color, number))
        # Action cards (two of each)
        for action in numbers[10:]: # Skip, Reverse, Draw Two
            deck.append(UnoCard(color, action))
            deck.append(UnoCard(color, action))

    # Wild cards (four of each)
    for _ in range(4):
        deck.append(UnoCard(None, 'Wild'))
        deck.append(UnoCard(None, 'Wild Draw Four'))

    random.shuffle(deck)
    return deck

def deal_initial_hands(deck, num_players=2, cards_per_player=7):
    hands = [[] for _ in range(num_players)]
    for _ in range(cards_per_player):
        for i in range(num_players):
            hands[i].append(deck.pop(0))
    return hands, deck

# --- Basic Game Structure ---
def play_uno(num_players=2):
    deck = create_uno_deck()
    hands, deck = deal_initial_hands(deck, num_players)
    discard_pile = []

    # Start with a card from the deck (must not be a wild card)
    while True:
        top_card = deck.pop(0)
        if top_card.color is not None: # Not a wild card
            discard_pile.append(top_card)
            break
        else:
            deck.append(top_card) # Return wild cards to the deck and shuffle

    print("--- Uno Game Started ---")
    print(f"Top card: {discard_pile[-1]}")

    current_player_index = 0
    direction = 1 # 1 for clockwise, -1 for counter-clockwise

    while True:
        current_player = current_player_index % num_players
        print(f"\nPlayer {current_player + 1}'s turn.")
        print(f"Your hand: {hands[current_player]}")
        print(f"Top card: {discard_pile[-1]}")

        # Simple player action: Try to play the first valid card
        played_card = None
        for i, card in enumerate(hands[current_player]):
            if card.can_play_on(discard_pile[-1]):
                played_card = hands[current_player].pop(i)
                discard_pile.append(played_card)
                print(f"Player {current_player + 1} played: {played_card}")
                break

        # If no card was played, draw a card
        if played_card is None:
            if not deck:
                # Reshuffle discard pile to create new deck (leaving top card)
                deck = discard_pile[:-1]
                random.shuffle(deck)
                discard_pile = [discard_pile[-1]]

            drawn_card = deck.pop(0)
            hands[current_player].append(drawn_card)
            print(f"Player {current_player + 1} drew a card.")
            # Simplified: Player can play the drawn card if it's valid
            if drawn_card.can_play_on(discard_pile[-1]):
                 print(f"Player {current_player + 1} can play the drawn card: {drawn_card}")
                 # To make it simple, we won't automatically play it here in this basic version
                 # A real game would ask the player if they want to play it.

        # Check for win condition (very basic: player has no cards)
        if not hands[current_player]:
            print(f"\nPlayer {current_player + 1} wins!")
            break

        # Move to the next player (simplified: no action card effects applied)
        current_player_index += direction

        # Basic loop termination (e.g., after a few turns for demonstration)
        # In a real game, this would only end when a player wins.
        # if current_player_index > 10: # Example to stop
        #    print("\nGame stopped after a few turns.")
        #    break

# To run the basic game (with 2 players):
# play_uno(num_players=2)
