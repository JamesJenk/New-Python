import random
import time
import ast

# Adjustable Variables
NUM_DECKS = 8
NUM_ROUNDS = 5
HAND_DELAY = 0 # seconds
RESHUFFLE_THRESHOLD = 52
DATA_FILE = "data.txt"
MAX_SPLITS = 4

pack = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
rev_pack = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}

# Load history from data file
def read_history(filename=DATA_FILE):
    history = []
    try:
        with open(filename, "r") as f:
            content = f.read().strip().split("\n\n")
            for block in content:
                lines = block.splitlines()
                data = {}
                for line in lines:
                    if line.startswith("Player:"):
                        data["player"] = ast.literal_eval(line[len("Player: "):])
                    elif line.startswith("Dealer:"):
                        data["dealer"] = ast.literal_eval(line[len("Dealer: "):])
                    elif line.startswith("Outcome:"):
                        data["outcome"] = line[len("Outcome: "):].strip()
                    elif line.startswith("Action:"):
                        data["action"] = line[len("Action: "):].strip()
                if data:
                    history.append(data)
    except FileNotFoundError:
        pass
    return history

def full_card_name(card):
    mapping = {'J': 'Jack', 'Q': 'Queen', 'K': 'King', 'A': 'Ace'}
    return mapping.get(card, card)

def hand_value(cards):
    val = sum(rev_pack[c] for c in cards)
    if "Ace" in cards and val <= 11:
        val += 10
    return val

def basic_strategy(player_hand, dealer_card):
    dealer_card = full_card_name(dealer_card)
    val = hand_value(player_hand)
    dealer_val = rev_pack[dealer_card]
    if len(player_hand) == 2 and rev_pack[player_hand[0]] == rev_pack[player_hand[1]]:
        return "Split"
    if val >= 17:
        return "Stand"
    elif val <= 11:
        if val == 11:
            return "Double Down"
        return "Hit"
    elif 12 <= val <= 16:
        if dealer_val >= 7:
            return "Hit"
        else:
            return "Stand"
    else:
        return "Stand"


def player_decision(player_hand, dealer_hand, history, explore_rate=0.2):
    similar = [h for h in history if h["player"] == player_hand and h["dealer"] == dealer_hand]

    if not similar:
        strategy = basic_strategy(player_hand, dealer_hand[0])
        print(f"No exact hand match found. Using basic strategy: {strategy}")
        return strategy

    print("Found exact past hands. Analysing outcomes...")

    # Aggregate outcomes by action
    action_stats = {}
    for h in similar:
        action = h["action"]
        outcome = h["outcome"].lower()
        if action not in action_stats:
            action_stats[action] = {"win": 0, "push": 0, "lose": 0}
        action_stats[action][outcome] += 1

    # Determine best action based on majority outcome (win > push > lose)
    def outcome_score(stats):
        # Prioritise win over push
        if stats["win"] > stats["push"]:
            return (stats["win"], 1, stats["push"], -stats["lose"])
        elif stats["win"] == stats["push"]:
            # If tie in win and push, prefer win
            return (stats["win"], 1, stats["push"], -stats["lose"])
        else:
            return (stats["win"], 0, stats["push"], -stats["lose"])

    best_action = max(action_stats, key=lambda a: outcome_score(action_stats[a]))
    best_stats = action_stats[best_action]

    # Check if best action is generally winning or tying
    if best_stats["win"] + best_stats["push"] > 0:
        print(f"Choosing historically best action: {best_action} (Wins: {best_stats['win']}, Ties: {best_stats['push']}, Losses: {best_stats['lose']})")
        return best_action

    # If best action is losing, avoid repeating it; pick any other action or fallback
    losing_actions = [a for a, s in action_stats.items() if s["lose"] > 0]
    alternatives = [a for a in action_stats if a not in losing_actions]

    if alternatives:
        chosen = random.choice(alternatives)
        print(f"Previous action(s) lost; picking alternative action: {chosen}")
        return chosen

    # As a last fallback, use basic strategy
    strategy = basic_strategy(player_hand, dealer_hand[0])
    print(f"All known actions lost; using basic strategy: {strategy}")
    return strategy

def evaluate(hand):
    value = sum(rev_pack[card] for card in hand)
    if "Ace" in hand and value <= 11:
        value += 10
    return value

def reshuffle():
    return pack * 4 * NUM_DECKS

def deal(deck):
    return [deck.pop(), deck.pop()]

def hit(deck, hand):
    hand.append(deck.pop())

def play():
    deck = reshuffle()
    history = read_history()
    session = 1
    shoe = 1
    round_num = 0

    with open(DATA_FILE, "a") as f:
        print(f"Starting Blackjack AI Simulator for {NUM_ROUNDS} rounds\n")

        for i in range(NUM_ROUNDS):
            if len(deck) < RESHUFFLE_THRESHOLD:
                deck = reshuffle()
                shoe += 1

            round_num += 1
            print(f"--- Round {round_num} ---")

            player_hands = [deal(deck)]
            dealer = deal(deck)
            outcomes = []
            actions_taken = []

            split_count = 0

            for hand in player_hands[:]:
                while True:
                    action = player_decision(hand, dealer, history)
                    actions_taken.append(action)

                    if action == "Split" and split_count < MAX_SPLITS:
                        if len(hand) == 2 and rev_pack[hand[0]] == rev_pack[hand[1]]:
                            split_count += 1
                            player_hands.remove(hand)
                            player_hands.append([hand[0], deck.pop()])
                            player_hands.append([hand[1], deck.pop()])
                            break
                        else:
                            action = "Hit"  # fallback if not valid to split
                    elif action == "Double Down" and len(hand) == 2:
                        hit(deck, hand)
                        break
                    elif action == "Hit" and evaluate(hand) < 21:
                        hit(deck, hand)
                        continue
                    else:
                        break

            while evaluate(dealer) < 17:
                hit(deck, dealer)

            for hand in player_hands:
                player_value = evaluate(hand)
                dealer_value = evaluate(dealer)

                if player_value > 21:
                    outcome = "Lose"
                elif dealer_value > 21 or player_value > dealer_value:
                    outcome = "Win"
                elif player_value == dealer_value:
                    outcome = "Push"
                else:
                    outcome = "Lose"

                f.write(f"Session: {session} Shoe: {shoe} Round: {round_num}\n")
                f.write(f"Player: {hand}\n")
                f.write(f"Dealer: {dealer}\n")
                f.write(f"Outcome: {outcome}\n")
                f.write(f"Action: {actions_taken.pop(0)}\n\n")

                print(f"Player: {hand} | Dealer: {dealer} | Outcome: {outcome} | Action: {action}\n")
                time.sleep(HAND_DELAY)

if __name__ == "__main__":
    play()
