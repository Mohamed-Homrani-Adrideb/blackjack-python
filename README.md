# Black Jack Game in Python

A simplified game of 21 made for Python!

## Card Values

Suits do not affect card values.

- 2 - 10 are worth the same as the card name.
- J, Q, and K are all worth 10.
- Aces: worth 11, unless that would put the hand over 21. Then the ace is worth 1. This is recalculated automatically every time a card is drawn.

## Gameplay

Simply run the script to begin playing. The hand begins with both the player and dealer receiving two cards. The player only sees one of the dealer's cards at the start.

The player goes first, choosing to **Hit (Press 1)** or **Stay (Press 0)**. If the player gets more than 21 points they are **Bust** and have lost the hand.

After the player selects Stay, it is the dealer's turn. The dealer reveals the hidden card and keeps hitting until their score is **17 or higher**. If the dealer goes over 21, the dealer is Bust and the player wins. Otherwise the higher score wins.

## Blackjack

A player gets a **Blackjack** if they are dealt a card worth 10 and an Ace at the beginning of the hand (21 with the first two cards). A Blackjack beats any other hand, unless the dealer also has a Blackjack.

## Results

| Situation | Result |
|-----------|--------|
| Player goes over 21 | Player loses |
| Dealer goes over 21 | Player wins |
| Player total is higher | Player wins |
| Dealer total is higher | Dealer wins |
| Same total | Push (tie) |

> **Note:** The purpose of this script is to let the user play a simple hand of Blackjack without some of the higher level parts of the game like betting, splitting or doubling down.

## Demo

```
Welcome to the BlackJack Game:

Dealer shows 3 of club and a hidden card

Your hand: 9 of club, K of heart  (total: 19)

Hit (press 1) or Stay (press 0): 0

Dealer's second card was 8 of diamond
Dealer's hand: 3 of club, 8 of diamond  (total: 11)
Dealer draws 6 of diamond

Dealer's hand: 3 of club, 8 of diamond, 6 of diamond  (total: 17)

You win! 19 vs 17
```

## Deployment

To run this project, you need Python 3 installed. Then run:

```
python blackjack.py
```
