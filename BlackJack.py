# Anna Rakes
# Blackjack Project

import random

#def CreateDeck
# Create the deck of cards as a list of dictionaries containing the 4 suits and the values 2-11 and ace,
# jack, queen, and king. For each combination, append it to a list. Each item in the list is a dictionary
# that contains the suit type and the card's value
def CreateDeck():
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
    values = ["Ace", "Jack", "Queen", "King"]
    for number in range(2,11):
        values.append(number)
    cardDeck=[]
    for type in suits:
        for item in values:
            dictionary = {}
            dictionary['suit']=type
            dictionary['number']=item
            cardDeck.append(dictionary)
    return cardDeck


# This function shuffles the deck created above. It creates a list of numbers 0 through 51 in a random order
# It then iterates through the random number list and takes the card from the unshuffled deck at the random
# number's index and adds it to a new card deck. This becomes the shuffled deck
def ShuffleDeck(deck):
    numberDeck=[]
    while len(numberDeck)<52:
        ranNum = random.randint(0,51)
        if ranNum not in numberDeck:
            numberDeck.append(ranNum)
    shuffledDeck = []
    for number in numberDeck:
        shuffledDeck.append(deck[number])
    return shuffledDeck


#def Deal2Cards
# A function that deals two cards by pulling them out of the card deck and adding them to the players hand.
# The cards are then removed from the deck. This returns the player's hand with two cards and the updated
# deck with the first two cards removed.
def Deal2Cards(player, deck):
    player.append(deck[0])
    deck.pop(0)
    player.append(deck[0])
    deck.pop(0)
    return player,deck


#def Deal1Card
# Used when the player chooses to hit. Adds a card from the deck to the players hand and then removes that
# first card from the deck. It returns the player's hand with the added card and the new deck with one less
# card.
def Deal1Card(player, deck):
    player.append(deck[0])
    deck.pop(0)
    return player,deck


# def DisplayDealerHand
# this function display's the dealers first card by taking the first item from the dealer's hand, which
# is a list of all of their cards.
def DisplayDealerHand(hand):
    firstCard = hand[0]
    print(f"The dealer's first card is a {firstCard["number"]} of {firstCard["suit"]}")


# def DisplayHand
# this function loops through the list of the player's hand of cards and prints out the suit of the
# card and it's value
def DisplayHand(playerHand, turn):
    if turn == "Computer" or turn == "Dealer":
        print(f"The {turn}'s hand consists of:")
    else:
        print("Your hand consists of:")
    count = 1
    for card in playerHand:
        print(f"Card {count}", end=": ")
        print(f"A {card["number"]} of {card["suit"]}")
        count +=1
    return None


# def CalculateScore
# This function loops through the player's cards in their hands. If the card is a face card, except ace,
# it creates a new key in that dictionary with the integer value of it, 10. If it is just a number, that number
# is added to the new integer key in that card's dictionary. This function also creates a variable called
# minusAceScore. This variable is the score of the player's hand, not including the ace. This is then used
# in the next for statement to decide whether the ace should be an 11 or 1. If the ace is 11 and added to the
# players minusAceScore and it causes their score to be over 21, the ace's dictionary will have the int key
# be a value of 1. If the ace is 11, however, and doesn't make their score go over 21, the card's int key value
# is stored as 11. If there are two aces in the player's hand, they are both assigned with an int value of 1.
# Once every card in the player's hand has a corresponding integer value in its dictionary, the values of all
# the cards in the player's hand are added up and returned.
def CalculateScore(playerHand):
    minusAceScore = 0
    faceCards = ["Jack", "Queen", "King"]
    for card in playerHand:
        if card["number"] in faceCards:
            card["int"] = 10
        elif (card["number"] not in faceCards) & (card["number"] != "Ace"):
            card["int"] = card["number"]
        if card["number"] != "Ace":
            minusAceScore += card["int"]
    count = 0
    for card in playerHand:
        if card["number"] == "Ace":
            count += 1
            if minusAceScore + 11 >21:
                card["int"] = 1
            else:
                card["int"] = 11
    if count == 2:
        for card in playerHand:
            if card["number"] == "Ace":
                card["int"]= 1
    score = 0
    for card in playerHand:
        score += card["int"]
    return score


# def Hit
# If the player chose to hit, this function will first deal them another card using the Deal1Card function.
# It will then display the player's updated hand by calling the display hand function. It will then calculate
# the player's updated score by calling the CalculateScore function. It will return their score, their new
# hand with the added card, and the new deck with one less card taken from the top.
def Hit(deck,hand,turn):
    hand,deck = Deal1Card(hand,deck)
    DisplayHand(hand,turn)
    score = CalculateScore(hand)
    return score, hand, deck


# def AfterHit
# once the player has chosen to hit, their new score needs to be interpreted. If the new card causes their
# score to be over 21, their turn will end. If they have 21, they are also done with their turn. if their
# score is less than 21, they continue their turn.
def AfterHit(score):
    if score > 21:
        choice = "end"
        print("Busted. You lose.")
    elif score == 21:
        print("You have 21")
        choice = "end"
    else:
        choice = "hit"
    return choice


# def PLayer1Turn
# Stores all the actions that player 1 will take.  Displays their starting hand, calculates their starting
# hand score. If their first hand dealt is 21, they win. If not, they will be asked to hit or stand. If they
# choose to stand, their turn is over and their score from their original hand, their original hand, and the deck
# is returned. If they choose to hit, the hit function and after hit function will be called. The after hit
# function returns their choice to continue hitting or end their turn. If their score is less than 21, the
# AfterHit function returned hit, continuing the while loop and asking them if they want to hit or stand.
# However, if the AfterHit function returned end, meaning they busted or got 21, the loop ends and their
# turn is over. Their updated hand, score, and deck is returned.
def Player1Turn(name,hand,deck):
    turn = name
    print("-"*25)
    print(f"It is {name.capitalize()}'s turn")
    DisplayHand(hand,turn)
    score = CalculateScore(hand)
    print(f"Your current score is {score}")
    if score == 21:
        print("You Win! The game has ended.")
    else:
        choice = "hit"
        while choice.lower() == "hit":
            choice = input("Do you want to Hit or Stand?")
            if choice.lower() == "stand":
                return score,hand, deck
            elif choice.lower() == "hit":
                score, hand, deck = Hit(deck,hand,turn)
                print(f"Your current score is {score}")
                choice = AfterHit(score)
        return score,hand,deck


# def ComputerTurn
# This function is the same as Player1Turn, except it automates when to hit or stand. If the computer's score
# is less than 13, it automatically chooses hit and calls the Hit function. If hitting caused them to bust,
# it ends the while loop. If it didn't, it allowed them to continue to hit or stand depending on their new
# # score. If their score was higher than 13 they stood and the while loop ended, ending their turn.
def ComputerTurn(hand, deck):
    turn = "Computer"
    print("-"*25)
    print("It is the computer's turn.")
    DisplayHand(hand,turn)
    score = CalculateScore(hand)
    print(f"The computer's score is {score}")
    if score == 21:
        print("The computer wins! The game has ended.")
    else:
        choice = "hit"
        while choice == 'hit':
            if score<13:
                print("The computer chose to hit")
                score, hand, deck = Hit(deck, hand,turn)
                print(f"The computer's score is {score}")
                if score > 21:
                    print("The computer busted")
                    choice = "end"
            elif score == 21:
                print("The computer got 21.")
                choice = "end"
            elif score>=13 and score<=21:
                print("The computer chose to stand")
                choice = 'end'
                return score, hand, deck
            elif score >21:
                print("The computer busted")
                choice = "end"
        return score,hand, deck


# def DealerTurn
# This function is the similar to ComputerTurn, but with different thresholds. If the dealer's score
# is less than 17, it automatically chooses hit and calls the Hit function. If hitting caused them to bust,
# it ends the while loop. If it didn't, it allowed them to continue to hit or stand depending on their new
# # score. If their score was higher than 15 they stood and the while loop ended, ending their turn.
def DealerTurn(hand, deck):
    turn = "Dealer"
    print("-"*25)
    print("It is the dealer's turn.")
    DisplayHand(hand,turn)
    score = CalculateScore(hand)
    print(f"The dealer's score is {score}")
    choice = "hit"
    while choice == 'hit':
        if score <= 16:
            print("The dealer chose to hit")
            score, hand, deck = Hit(deck, hand,turn)
            print(f"The dealer's score is {score}")
            if score >21:
                print("The dealer busted")
                choice = "end"
        elif score == 21:
            print("The dealer got 21.")
            choice = "end"
        elif (score >=16) and (score<=21):
            print("The dealer chose to stand")
            choice == 'end'
            return score, hand, deck
        elif score >21:
            print("The dealer busted")
            choice = "end"
    return score, hand, deck


# def DetermineWinner
# This function determines the winner for the 2 player game. It takes the player's name and all three
# players score and determines the winners. The results are stored into a dictionary with player's result
# and the computer's result.
def DetermineWinner(player1name, player1Score, computerScore, dealerScore):
    #player1
    if (player1Score > dealerScore and player1Score<22) or (player1Score<=21 and dealerScore>21):
        player1result = "Won"
    elif (player1Score>21) or (player1Score<dealerScore and dealerScore<=21):
        player1result = "Lost"
    elif player1Score==dealerScore and player1Score<=21 and dealerScore<=21:
        player1result = "Draw"
    #computer
    if (computerScore > dealerScore and computerScore<22) or (computerScore<=21 and dealerScore>21):
        computerResult = "Won"
    elif (computerScore>21) or (computerScore<dealerScore and dealerScore<=21):
        computerResult = "Lost"
    elif computerScore==dealerScore and computerScore<=21 and dealerScore<=21:
        computerResult = "Draw"
    results = {player1name:player1result,"computer":computerResult}
    return results


#def Determine1Winner
# This function determines the winner for the 1 player game. It takes the player's name and the player
# # and dealer's score. The results are stored into a dictionary with player's result.
def Determine1Winner(player1name,player1Score,dealerScore):
    if (player1Score > dealerScore and player1Score<22) or (player1Score<21 and dealerScore>21):
        player1result = "Won"
    elif (player1Score>21) or (player1Score<dealerScore and dealerScore<21):
        player1result = "Lost"
    elif player1Score==dealerScore and player1Score<21 and dealerScore<21:
        player1result = "Draw"
    results = {player1name:player1result}
    return results


# def TwoPlayer
# This function contains most of the game play for the two player game. It creates the deck, shuffles it,
# intializes the players' hand's and deals them each two cards. It then display's the dealer's first card.
# It then calls each of the player's function turns: PLayer1Turn, ComputerTurn, and DealerTurn. Once they
# have all made their turn, the final results are determined and printed. It then asks if they want to play
# again. If they don't want to, the while loop containing all the steps is terminated.
def TwoPlayer():
    playerName = input("What is your name?")
    gamePlay = 'yes'
    while gamePlay.lower() == 'yes':
        unshuffledDeck = CreateDeck()
        shuffledDeck = ShuffleDeck(unshuffledDeck)
        player1Hand = []
        computerHand = []
        dealerHand = []
        player1Hand, shuffledDeck = Deal2Cards(player1Hand, shuffledDeck)
        computerHand, shuffledDeck = Deal2Cards(computerHand, shuffledDeck)
        dealerHand, shuffledDeck = Deal2Cards(dealerHand, shuffledDeck)
        DisplayDealerHand(dealerHand)
        player1Score, player1Hand, shuffledDeck = Player1Turn(playerName,player1Hand,shuffledDeck)
        computerScore, computerHand, shuffledDeck = ComputerTurn(computerHand,shuffledDeck)
        dealerScore, dealerHand, shuffledDeck = DealerTurn(dealerHand,shuffledDeck)
        finalResults = DetermineWinner(playerName,player1Score,computerScore,dealerScore)
        print("GAME RESULTS:")
        for key,value in finalResults.items():
            print(f"{key}:{value}")
        gamePlay = input("Do you want to play another hand? 'Yes' or 'No'?")


# def OnePlayer
# This function contains most of the game play for the one player game. It creates the deck, shuffles it,
# intializes the player and dealer's hand, and deals them each two cards. It then display's the dealer's first
# card. It then calls each of the player's function turns: PLayer1Turn and DealerTurn. Once they
# have  made their turn, the final results are determined and printed. It then asks if they want to play
# again. If they don't want to, the while loop containing all the steps is terminated.
def OnePlayer():
    playerName = input("What is your name?")
    gamePlay = 'yes'
    while gamePlay.lower() == 'yes':
        unshuffledDeck = CreateDeck()
        shuffledDeck = ShuffleDeck(unshuffledDeck)
        player1Hand = []
        dealerHand = []
        player1Hand, shuffledDeck = Deal2Cards(player1Hand, shuffledDeck)
        dealerHand, shuffledDeck = Deal2Cards(dealerHand, shuffledDeck)
        DisplayDealerHand(dealerHand)
        player1Score, player1Hand, shuffledDeck = Player1Turn(playerName, player1Hand, shuffledDeck)
        dealerScore, dealerHand, shuffledDeck = DealerTurn(dealerHand, shuffledDeck)
        finalResults = Determine1Winner(playerName, player1Score, dealerScore)
        print("GAME RESULTS:")
        for key, value in finalResults.items():
            print(f"{key}:{value}")
        gamePlay = input("Do you want to play another hand? 'Yes' or 'No'?")


# The main program determines if it is a one or two player game and calls the corresponding function
if __name__ == "__main__":
    try:
        game = int(input("Do you want to play a 1-player game or a 2-player game. Type 1 or 2."))
    except:
        game = int(input("You did not enter a valid number. Enter 1 or 2."))
    if game == 2:
        TwoPlayer()
    elif game == 1:
        OnePlayer()


