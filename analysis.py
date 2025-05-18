#!/bin/python3

import re
from collections import defaultdict

DATA_FILE = 'data.txt'

def load_data():
    data = []
    current_shoe = None
    current_hand = None
    entry = {}

    with open(DATA_FILE, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            if line.startswith('--- Shoe'):
                current_shoe = int(re.search(r'Shoe (\d+)', line).group(1))
            elif line.startswith('Hand'):
                if all(k in entry for k in ('player_hand', 'dealer_hand', 'outcome')):
                    data.append(entry)
                current_hand = int(re.search(r'Hand (\d+)', line).group(1))
                entry = {'shoe': current_shoe, 'hand': current_hand}
            elif line.startswith('Player:'):
                entry['player_hand'] = eval(line.split(': ')[1])
            elif line.startswith("Dealer:"):
                entry['dealer_hand'] = eval(line.split(': ')[1])
            elif line.startswith("Outcome:"):
                entry['outcome'] = line.split(': ')[1]

        if all(k in entry for k in ('player_hand', 'dealer_hand', 'outcome')):
            data.append(entry)

    return data

def analyse_data(data):
    total_games = len(data)
    outcomes = defaultdict(int)
    hand_stats = defaultdict(lambda: defaultdict(int))

    for entry in data:
        outcomes[entry['outcome']] += 1
        hand_value = sum(min(10, card_to_value(c)) for c in entry['player_hand'])
        hand_stats[hand_value][entry['outcome']] += 1

    print("--- Summary ---")
    print(f"Total Games: {total_games}")
    for outcome, count in outcomes.items():
        print(f"{outcome}: {count} ({count/total_games:.1%})")

    print("\n--- Outcomes by Player Hand Value ---")
    for val in sorted(hand_stats):
        print(f"Hand Value {val}:")
        total = sum(hand_stats[val].values())
        for outcome, count in hand_stats[val].items():
            print(f"  {outcome}: {count} ({count/total:.1%})")

def card_to_value(card):
    if card == 'Ace':
        return 1
    elif card in ['Jack', 'Queen', 'King']:
        return 10
    else:
        try:
            return int(card)
        except ValueError:
            return 0

if __name__ == '__main__':
    data = load_data()
    analyse_data(data)
