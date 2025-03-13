#Blackjack Project

##Author: Anna Rakes

###Overview

This project is a Python implementation of the classic card game Blackjack, developed for a Computer Science 1 class. The game supports both single-player mode (against the dealer) and two-player mode (against a computer opponent and the dealer). Players can choose to hit or stand based on their hand value, with the goal of getting as close to 21 as possible without going over.

###Features

Deck Creation: Generates a standard deck of 52 playing cards.

Shuffling Mechanism: Ensures random card distribution.

Game Modes:

Single-Player Mode: Player competes against a dealer.

Two-Player Mode: Player competes against a computer opponent and a dealer.

Game Logic:

Deals initial hands to players and dealer.

Allows players to hit (draw another card) or stand (keep their current hand).

Implements dealer rules (hits on 16 or below, stands on 17 or above).

Determines game outcomes (win, lose, draw) based on Blackjack rules.

Interactive Gameplay: Players input choices via the console.

###How to Run

1. Install Python (if not already installed) – Download Python

2. Clone this repository:

git clone https://github.com/yourusername/blackjack-project.git

3. Navigate to the project directory:

cd blackjack-project

4. Run the game:

python blackjack.py

5. Follow the prompts to choose between a single-player or two-player game.

###Code Structure

CreateDeck(): Generates the deck as a list of dictionaries.

ShuffleDeck(deck): Shuffles the deck randomly.

Deal2Cards(player, deck): Deals two cards to a player.

Deal1Card(player, deck): Deals one additional card (used when hitting).

CalculateScore(playerHand): Computes the player's current score based on card values.

Player1Turn(): Handles player input for hitting or standing.

ComputerTurn(): Automates the computer’s gameplay decisions.

DealerTurn(): Implements dealer rules.

DetermineWinner(): Determines the final game outcome.

Main Function: Asks the user to choose between single-player or two-player mode and starts the game.


###License

This project is for educational purposes and is open for modification and improvement.

Enjoy the game and feel free to contribute!
