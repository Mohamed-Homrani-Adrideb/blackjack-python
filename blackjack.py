import random as rn

RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
SUITS = ['spade', 'heart', 'diamond', 'club']


# Build a shuffled deck___________________________________
def make_deck():
    deck = [[s, r] for s in SUITS for r in RANKS]
    rn.shuffle(deck)
    return deck


# Value of a hand (Ace is 11 or 1 automatically)__________
def hand_value(hand):
    total = 0
    aces = 0
    for _, rank in hand:
        if rank in ('J', 'Q', 'K'):
            total += 10
        elif rank == 'A':
            total += 11
            aces += 1
        else:
            total += rank
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total


# Nice printing of a hand_________________________________
def show(hand):
    return ', '.join(f"{r} of {s}" for s, r in hand)


# Player's turn: returns the final result or None to continue
def players_turn(deck, player, dealer):
    while True:
        total = hand_value(player)
        print(f"Your hand: {show(player)}  (total: {total})")

        if total == 21:
            if len(player) == 2:
                print("BLACKJACK!")
            else:
                print("You made 21!")
            return 'stay'
        if total > 21:
            print("You got Bust.....You Lost\n")
            return 'bust'

        choice = input("\nHit (press 1) or Stay (press 0): ").strip()
        if choice == '1':
            card = deck.pop()
            player.append(card)
            print(f"\nYou draw {card[1]} of {card[0]}\n")
        elif choice == '0':
            return 'stay'
        else:
            print("Enter a valid number (1 or 0)....\n")


# Dealer's turn: hits until 17 or more____________________
def dealers_turn(deck, dealer):
    print(f"\nDealer's second card was {dealer[1][1]} of {dealer[1][0]}")
    while True:
        total = hand_value(dealer)
        print(f"Dealer's hand: {show(dealer)}  (total: {total})")
        if total >= 17:
            return total
        card = deck.pop()
        dealer.append(card)
        print(f"Dealer draws {card[1]} of {card[0]}\n")


def play():
    print("Welcome to the BlackJack Game:\n")
    deck = make_deck()
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]

    print(f"Dealer shows {dealer[0][1]} of {dealer[0][0]} and a hidden card\n")

    result = players_turn(deck, player, dealer)
    if result == 'bust':
        return

    player_total = hand_value(player)
    player_blackjack = (player_total == 21 and len(player) == 2)

    dealer_total = dealers_turn(deck, dealer)
    dealer_blackjack = (dealer_total == 21 and len(dealer) == 2)

    print()
    if dealer_total > 21:
        print("Dealer got Busted\nYou Won!\n")
    elif player_blackjack and not dealer_blackjack:
        print("Blackjack beats the dealer.....You Won!\n")
    elif dealer_blackjack and not player_blackjack:
        print("Dealer got a BlackJack.....You Lost\n")
    elif player_total > dealer_total:
        print(f"You win! {player_total} vs {dealer_total}\n")
    elif player_total < dealer_total:
        print(f"Dealer wins! {dealer_total} vs {player_total}\nBetter Luck Next Time!\n")
    else:
        print(f"It's a push (tie) at {player_total}\n")


if __name__ == '__main__':
    play()
