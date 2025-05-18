#!/bin/python3

# Increase font size

from random import randint
from time import sleep

def shuffle():

    # List of possible cards to generate deck

    pack = {
        1 : "Ace",
        2 : "Two",  
        3 : "Three",
        4 : "Four",
        5 : "Five",
        6 : "Six",
        7 : "Seven",
        8 : "Eight",
        9 : "Nine",
        10 : "Ten",
        11 : "Jack",
        12 : "Queen",
        13 : "King",
        }

    # To create "box" which is the deck

    # There is a dictionary of 13 values which is then shuffled and appended, this then is done 4 times which adds up to 52
    # There will not be repeats of the samae card for each 13 shuffled allowing 4 of every value to be in each deck.

    repeat = []
    deck = []
    box = []

    for i in range(0, 4):

        while len(repeat) < 13:
            card = pack[randint(1, 13)]

            if card in repeat:
                None
            
            else:
                deck.append(card)
                repeat.append(card)

        for i in deck:
            box.append(i)

    deck = []
    repeat = []

    return box
    

    first_sym = symbol[randint(0,1)]
    second_sym = symbol[randint(2,3)]

def showhand(deck, type = 1):

    # Symbols are purely visual and not assigned as suit doesn't mean anything in blackjack

    symbol = ["♥", "♦", "♣", "♠"]

    # Type allows the function to be appplied to show both the dealer's and user's hands

    if type == 1:
        print("Your hand is:", end = " ")

    else:
        print("Dealer's hand is:", end = " ")

    sleep(1)

    # Iterates through the list of the chosen hand and prints to for visual ease

    for card in deck:
        print(symbol[randint(0, 3)], card, end = " ")
    
    # Function shows both hand and value for those new to blackjack, evaluate is defined later

    val = evaluate(deck)

    print("")

    if type == 1:
        print("Your hand value is:", val)

    else:
        print("Dealer's hand value is:", val)

    sleep(1)

    return None

def deal(deck, deals = 1):

    # Adds a card to chosen hand and then deletes card from deck

    for card in range(0, int(deals)):
        deck.append(box[0])
        box.pop(0)

    return deck

def evaluate(deck = []):

    # To calculate the value of your hand

    val = 0
    
    for card in deck:
        val += rev_pack[card]

    # To check the special case of aces

    if "Ace" in deck and val <= 11:
        val += 10

    if "Ace" in deck and val > 21 and len(ac) > 1:
        val -= 10
        ac.append(1)

        print(ace_count)

    return val

def finish():

    # Print statement at end of code

    print("")
    print(f"Your current balance is ${bank}")
    print("-------------------")
    print("Blackjack Simulator")

def play(deck = [], bet = 1):

    # Options to play game

    while True:
            sleep(1)

            choice = input("Which do you choose?: ")

            # If you choose to keep your cards this part of the programme ends and you go against the dealer

            if choice == "Stand" or choice == "stand" or choice == "s" or choice == "2" or choice == "S":
                break

            # If you choose to take another card and you go over 21 this ends and you go against the dealer
            # Otherwise continue playing

            if choice == "Hit" or choice == "hit" or choice == "h" or choice == "1" or choice == "H":
                deal(deck)
                showhand(deck)
                value = evaluate(deck)
                nodub = False

                if value <= 20:
                    print("Hit or Stand?")

                elif value > 21:
                    break

                else:
                    break

            if choice == "Double Down" or choice == "double down" or choice == "dd" or choice == "3" or choice == "DD" and nodub == False:

                # Doubles your bet but you recieve one card and one card alone

                deal(deck)
                showhand(deck)
                value = evaluate(deck)
                bet *= 2
                break

            # To try and catch any cheaters attempting a double down after a hit

            elif nodub == True:
                print("You can't double down after a hit!")

            else:
                print("Your input is off.")
                print("Try again!")
    
    return deck, bet

def results(deck = [], bet = 1, bank = 1):

    # After choices are made and assuming you didn't bust, it is the dealer's turn
    # The dealer then hits until soft 17
    # Then standard blackjack rules apply
    
    value = evaluate(deck)
    del_val = evaluate(dealer)

    if value > 21:
        print("Bust! You lose.")
        bank -= bet

        return bank

    while del_val < 17:

        deal(dealer)
        showhand(dealer, 2)
        del_val = evaluate(dealer)

    if del_val > 21:
        print("Dealer bust! You win.")
        bank += bet

    elif value > del_val:
        print("You win.")
        bank += bet

    elif value < del_val:
        print("You lose.")
        bank -= bet

    else:
        print("Push!")

    return bank

# Reversed dictionary of deck to calculate card value
    
rev_pack = {
    "Ace" : 1,
    "Two" : 2,
    "Three" : 3,
    "Four": 4,
    "Five" : 5,
    "Six" : 6,
    "Seven" : 7,
    "Eight" : 8,
    "Nine" : 9,
    "Ten" : 10,
    "Jack" : 10,
    "Queen" : 10,
    "King" : 10
}

# To begin the game

# cont is short for continue which is asked at the end to check if you want to keep playing
# symbols are used for dealers hand

cont = 'y'
symbol = ["♥", "♦", "♣", "♠"]

while cont == "y":

    print("Blackjack Simulator")
    print("-------------------")
    print("")
    print("Let's play!")
    print("")
    print("Your bank will always start with $1")
    print("")

    # rules are a choice for first time players

    rules = input("Do you want to see the rules? (y/n): ")

    if rules == "y":
        print("")
        print("Single deck blackjack.")
        print("Deck shuffles after each hand.")
        print("Maximum bet: $10,000.")
        print("Minimum bet: $1.")
        print("Dealer stands on soft 17.")
        print("The goal of blackjack is to get as close to twenty-one as possible without going over.")
        print("While also having a higher hand value than the dealer.")
        print("You may only see the first of the two cards the dealer holds during play.")
        print("You are dealt two cards and you have the options to 'Hit', 'Double Down', or 'Stand'.")
        print("You may not split.")
        print("Hit: You gain another card.")
        print("Other input options for 'Hit': Hit, hit, h, H, 1")
        print("Stand: You stay with the cards and compare to the dealer.")
        print("Other input options for 'Stand': Stand, stand, s, S, 2")
        print("Double Down: You get hit once and your bet doubles.")
        print("Other input options for 'Double Down': Double Down, double down, dd, DD, 3")

    # Allows you to play as many loops as possible without having to see the start each time

    rounds = int(input("How many hands do you want to play?: "))
    box = shuffle()
    bank = 1

    # If you go to $50 in debt the programme ends for everyone's sake

    addict = False

    sleep(1)

    for i in range(0, rounds):

        ac = []

        print("")
        print(f"Your current balance is ${bank}")
        print("")

        bet = int(input("What is your bet this round? $"))

        # max bet is $10,000 min bet is $1

        if bet > 10000:
            print("Your bet is too large.")
            bet = int(input("What is your bet this round? $"))

        elif bet < 1:
            print("Your bet is too small.")
            bet = int(input("What is your bet this round? $"))

        end = False

        # To help calculate ace value and prevent a constant deduction of 11 everytime the hand goes over 21 and there is an ace in it

        ace_count = 0

        print("")
        print("Great! Here is your hand:")

        # Dealer's hand

        dealer = []
        dealer = deal(dealer, 2)

        # Dealing hand

        hand = []
        hand = deal(hand, 2)
        ac = []
        # Showing cards

        showhand(hand)
        print("Dealer's topcard: ", symbol[randint(0,3)], dealer[0])

        # To calculate hand value

        value = evaluate(deck = hand)

        sleep(1)

        # Dealer's value

        del_val = evaluate(deck = dealer)

        # To check for blackjack

        if value == 21:
            print("Blackjack! You win.")
            bank += bet
            finish()
            continue
        
        # Standard blackjack optionsb

        # Seeing the new hand after play and checking the bet wasn't doubled in a double down

        hand, bet = play(hand, bet = bet)

        showhand(dealer, 2)

        sleep(1)

        # Bank is recalculated after results finished

        bank = results(bank = bank, bet = bet, deck = hand)

        sleep(1)

        finish()

        # To help those in need

        if bank <= -50:
            print("You have a problem.")
            print("We're cutting you off.")
            print("However, they say ninety-nine pecent of gamblers quit before their big win.")
            print("So run the programme again and we will gladly take more of your money.")

            finish()

            addict = True

            break

        if addict == True:
            break

        # Reshuffling after each hand

        shuffle()

        sleep(1)

    cont = 'n'
    cont = input("Would you like to keep playing? (y/n): ")