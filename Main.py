# Main.py
from sys import argv
from UnoEngine import Uno
from Player import Player
from UnoDeck import UnoDeck
import os
import csv 

class Main:
    def __init__(self, num_games, game_seed, player_seed):
        num_players_initialized = 10 
        players = []
        stats = [0] * num_players_initialized 
        strategy = ['wild_card_strategy', 'change_color_strategy',
                    'same_color_strategy', 'random_strategy']

        print("--- Initializing Game Simulation--")

        player_names_for_report = []

        for i in range(num_players_initialized):
            player_name = f"Player {i+1}"
            player_names_for_report.append(player_name)
            
            if i < 4:
                players.insert(i, Player(player_name, [strategy[i]], player_seed))
            elif i == 4: # Player 5
                players.insert(i, Player(player_name, [strategy[0], strategy[1]], player_seed))
            elif i == 5: # Player 6
                players.insert(i, Player(player_name, [strategy[0], strategy[2]], player_seed))
            elif i == 6: # Player 7
                players.insert(i, Player(player_name, [strategy[1], strategy[0]], player_seed))
            elif i == 7: # Player 8
                players.insert(i, Player(player_name, [strategy[1], strategy[2]], player_seed))
            elif i == 8: # Player 9
                players.insert(i, Player(player_name, [strategy[2], strategy[0]], player_seed))
            elif i == 9: # Player 10
                players.insert(i, Player(player_name, [strategy[2], strategy[1]], player_seed))


        deck = UnoDeck(game_seed)

        for i in range(num_games):

            uno = Uno(players, deck) 
            print(f"\n--- Starting Game {i + 1} ---")
            winner_index = uno.start_game()
            if winner_index is not None:
                stats[winner_index] += 1
            deck.reset_deck()

        print("\n--- Simulation Complete ---")
        print("\n--- Final Scores ---")

        print("\n--- Player Wins ---")
        for i, player in enumerate(players):
            print(f"Player {player.name}: {stats[i]} Wins")

        print("\n--- Player Strategies ---")
        for player in players:
            print(f"Player {player.name}: {player.strategies}")

        self.generate_report(num_games, game_seed, players, stats, player_names_for_report)

    def generate_report(self, num_games, global_seed, players, stats, all_player_names):
        report_filename = "uno_simulation_summary.csv"
        
        header = ["Global_Seed", "Total_Games"] + all_player_names
        
        data_row = [str(global_seed), str(num_games)]
        
        current_players_in_simulation_names = {p.name for p in players}

        for player_name_in_header in all_player_names:
            found_player = False
            for i, player_obj in enumerate(players):
                if player_obj.name == player_name_in_header:
                    found_player = True
                    wins = stats[i]
                    data_row.append(str(wins))
                    break
            if not found_player:
                # Este caso seria para players que estão no cabeçalho mas não foram criados/passados para 'players'
                # na instância atual da Main.
                data_row.append("X") 


        file_exists = os.path.exists(report_filename)
        
        with open(report_filename, 'a', newline='') as f:
            writer = csv.writer(f)
            
            if not file_exists or os.stat(report_filename).st_size == 0:
                writer.writerow(header)
            
            writer.writerow(data_row)
        
        print(f"\n--- Simulation Report Saved to {report_filename} ---")


if __name__ == '__main__':
    if len(argv) < 4:
        print("Usage: python3 Main.py <number_of_games> <deck_seed_value> <player_seed_value>")
        print("Example: python3 Main.py 5 12345 67890")
        exit(1)
    try:
        num_games = int(argv[1])
        game_seed = int(argv[2])
        player_seed = int(argv[3])
    except ValueError:
        print("Error: number_of_games and seed values must be integers.")
        print("Usage: python3 Main.py <number_of_games> <deck_seed_value> <player_seed_value>")
        exit(1)
    
    Main(num_games, game_seed, player_seed)