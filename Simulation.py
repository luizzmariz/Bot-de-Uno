import csv
import os
import random
from collections import Counter

from Player import Player
from UnoDeck import UnoDeck
from UnoEngine import Uno


STRATEGY_MAP = {
        "R" : ["random_strategy"],
        "WC" : ["wild_card_strategy"],
        "SC" : ["same_color_strategy"],
        "CC" : ["change_color_strategy"],
        "WC+SC" : ["wild_card_strategy", "same_color_strategy"],
        "SC+WC" : ["same_color_strategy", "wild_card_strategy"],
        "WC+CC" : ["wild_card_strategy", "change_color_strategy"],
        "CC+WC" : ["change_color_strategy", "wild_card_strategy"],
        "SC+CC" : ["same_color_strategy", "change_color_strategy"],
        "CC+SC" : ["change_color_strategy", "same_color_strategy"]
    }
EXPERIMENTS_BASIC_GROUPS = [
        {
            "name": "Basic group: WC vs R",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["WC"], STRATEGY_MAP["R"]]
        },
        {
            "name": "Basic group: SC vs R",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["SC"], STRATEGY_MAP["R"]]
        },
        {
            "name": "Basic group: CC vs R",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["CC"], STRATEGY_MAP["R"]]
        },
        {
            "name": "Basic group: WC vs SC",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["WC"], STRATEGY_MAP["SC"]]
        },
        {
            "name": "Basic group: WC vs CC",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["WC"], STRATEGY_MAP["CC"]]
        },
        {
            "name": "Basic group: SC vs CC",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["SC"], STRATEGY_MAP["CC"]]
        }
    ]
EXPERIMENTS_SMALL_GROUPS = [
        {
            "name": "Small group: All random",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["R"], STRATEGY_MAP["R"], STRATEGY_MAP["R"],  STRATEGY_MAP["R"]]
        },
        {
            "name": "Small group: One from each base",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["R"], STRATEGY_MAP["WC"], STRATEGY_MAP["SC"],    STRATEGY_MAP["CC"]]
        },
        {
            "name": "Small group: Based vs Combined - WC and SC",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["WC"], STRATEGY_MAP["SC"], STRATEGY_MAP["WC+SC"],    STRATEGY_MAP["SC+WC"]]
        },
        {
            "name": "Small group: Based vs Combined - WC and CC",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["WC"], STRATEGY_MAP["CC"], STRATEGY_MAP["WC+CC"],    STRATEGY_MAP["CC+WC"]]
        },
        {
            "name": "Small group: Based vs Combined - CC and SC",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["CC"], STRATEGY_MAP["SC"], STRATEGY_MAP["CC+SC"],    STRATEGY_MAP["SC+CC"]]
        },

    ]
EXPERIMENTS_BIG_GROUPS = [
        {
            "name": "Big group: All strategies",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["CC"], STRATEGY_MAP["CC+SC"], STRATEGY_MAP["CC+WC"], STRATEGY_MAP["R"], STRATEGY_MAP["SC"], STRATEGY_MAP["SC+CC"], STRATEGY_MAP["SC+WC"], STRATEGY_MAP["WC"], STRATEGY_MAP["WC+CC"], STRATEGY_MAP["WC+SC"]]
        },
        {
            "name": "Big group: Dominant Strategy WC",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["WC"], STRATEGY_MAP["WC"], STRATEGY_MAP["WC"],   STRATEGY_MAP["R"], STRATEGY_MAP["SC"], STRATEGY_MAP["CC"]]
        },
        {
            "name": "Big group: Dominant Strategy SC",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["SC"], STRATEGY_MAP["SC"], STRATEGY_MAP["SC"],   STRATEGY_MAP["R"], STRATEGY_MAP["WC"], STRATEGY_MAP["CC"]]
        },
        {
            "name": "Big group: Dominant Strategy CC",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["CC"], STRATEGY_MAP["CC"], STRATEGY_MAP["CC"],   STRATEGY_MAP["R"], STRATEGY_MAP["SC"], STRATEGY_MAP["WC"]]
        },
        {
            "name": "Big group: Duplicants ",
            "num_games": 10000,
            "player_strategies": [STRATEGY_MAP["R"], STRATEGY_MAP["WC"], STRATEGY_MAP["SC"],    STRATEGY_MAP["CC"], STRATEGY_MAP["R"], STRATEGY_MAP["WC"], STRATEGY_MAP["SC"],     STRATEGY_MAP["CC"]]
        },
    ]

def run_simulation(experiment_name, num_games, player_strategies, global_seed=None):
    print(f"\n--- Running simulation: {experiment_name} ({num_games} games) ---")

    if global_seed is not None:
        random.seed(global_seed)
    else:
        random.seed()

    wins_by_player = Counter()

    for i in range(num_games):
        deck_seed = random.randint(0, 2**32-1)
        random_player_seed = random.randint(0, 2**32-1)

        deck_rng_instance = random.Random(deck_seed)
        random_player_rng_instance = random.Random(random_player_seed)

        deck = UnoDeck(deck_rng_instance)
        players = []

        for j, strategy in enumerate(player_strategies):
            players.append(Player(f"Bot {j+1}", strategy, random_player_rng_instance))

        game = Uno(players, deck)

        winner = game.start_game()
        wins_by_player[winner] += 1

    generate_report(experiment_name, num_games, wins_by_player, players, global_seed)

def generate_report(experiment_name, num_games, wins_by_player, players, global_seed):
        report_filename = "uno_simulation_summary.csv"

        header = [
            [],
            [f"Experiment: {experiment_name}"], 
            [f"Global seed: {global_seed}"],
            [f"Total_Games: {num_games}"],
        ]

        players_data = []

        for player in players:
            players_data.append(player.name)

        data_row = []

        for player in wins_by_player:
           data_row.append(str(wins_by_player[player]))
        
        file_exists = os.path.exists(report_filename)

        with open(report_filename, 'a', newline='') as f:
            writer = csv.writer(f)

            if not file_exists or os.stat(report_filename).st_size == 0:
                writer.writerow(["Uno Bot Simulation Results"])
            writer.writerows(header)
            writer.writerow(players_data)
            writer.writerow(data_row)
        #print(f"\n--- Simulation Report Saved to {report_filename} ---")

if __name__ == '__main__':
    GLOBAL_SEED = 10001

    for exp in EXPERIMENTS_BASIC_GROUPS:
        run_simulation(
            exp["name"],
            exp["num_games"],
            exp["player_strategies"],
            GLOBAL_SEED
        )