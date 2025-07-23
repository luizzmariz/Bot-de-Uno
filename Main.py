
from sys import argv
from UnoEngine import Uno
from Player import Player
from UnoDeck import UnoDeck


class Main:
    def __init__(self, num_games, game_seed, player_seed):
        num_players = 4
        players = []
        stats = [0,0,0,0,0,0,0,0,0,0]
        strategy = ['wild_card_strategy', 'change_color_strategy', 'same_color_strategy', 'random_strategy']
        print("--- Initializing Game Simulation ---")

        for i in range(num_players):
            players.insert(i, Player(f"Player {i+1}", [strategy[i]], player_seed))

        players.insert(5, Player("Player 5", [strategy[0], strategy[1]], player_seed))
        players.insert(6, Player("Player 6", [strategy[0], strategy[2]], player_seed))
        players.insert(7, Player("Player 7", [strategy[1], strategy[0]], player_seed))
        players.insert(8, Player("Player 8", [strategy[1], strategy[2]], player_seed))
        players.insert(9, Player("Player 9", [strategy[2], strategy[0]], player_seed))
        players.insert(10, Player("Player 10", [strategy[2], strategy[1]], player_seed))

        deck = UnoDeck(game_seed)

        for i in range(num_games):
            uno = Uno(players, deck)

            print(f"\n--- Starting Game {i + 1} ---")

            winner = uno.start_game()
            
            stats[winner] += 1

            deck.reset_deck()
        
        print("\n--- Simulation Complete ---")
        print("\n--- Final Scores ---")
        print("\n--- Player --- | --- Wins --- | --- Strategies ---")

        for i in players:
            print(f"    {i.name}   |      {stats[players.index(i)]}       |     {i.strategies}")


if __name__ == "__main__":
    if len(argv) < 4:
        print("Usage: python3 Main.py <number_of_games> <deck_seed_value> <player_seed_value>")
        print("Example: python3 Main.py 5 12345")
        exit(1)

    try:
        num_games = int(argv[1]) 
        game_seed = int(argv[2])
        player_seed = int(argv[3])
    
    except ValueError:
        print("Error: number_of_games and seed_value must be integers.")
        print("Usage: python3 Main.py <number_of_games> <deck_seed_value> <player_seed_value>")
        exit(1)

    Main(num_games, game_seed, player_seed)