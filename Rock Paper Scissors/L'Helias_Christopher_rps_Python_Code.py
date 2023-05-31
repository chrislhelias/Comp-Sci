# Author: Christopher L'Helias
# Date: 3/9/23
# Description: This is a game of rock paper scissors between a player and a computer. 
# The computer will initially tell the player how to stop the game and ask the player what move they would like to play. 
# Once the player selects a weapon, the computer will then choose a random response. 
# Depending on the response and the initial weapon choice, the computer will then say the game was either a win, loss, or draw. 
# If it is a win for the player, one point will be added to their score. If it is a win for the computer, one point will be added to its score. 
# If it is a draw, no points are added. After every round the computer will ask the player if they would like to see a scoreboard. 
# If yes, the computer prints a scoreboard that tallies points across all rounds that have been played.
# After every round, the computer will remind the player how to end the game. (by tying "stop")
# The computer will also inform the player if the enter in a unnaccepted and answer and will ask the player to try again.
# Challenges: The game determines who wins each round. 
# The game keeps score over multiple rounds and will ask if the player wants to see a scoreboard.
# Multple different user errors are addressed and user is told to enter a valid response.
# Bugs: The player will not be able to type stop and quit the game if it is not the beginning of a round.
# Sources: none

import random # import random module

moves = ["rock", "paper", "scissors"] # List of move choices
pscore = 0 # Player score initially starts off at 0
cscore = 0 # Computer score intially starts off at 0
valid_responses = ["rock", "paper", "scissors", "yes", "no"] # alid responses are rock, paper, scissors, yes, and no
while True: # creates loop
    user_rps = input("Enter stop to end. Lets play rock, paper, scissors, please choose your weapon (Rock, Paper, or Scissors)") # The variable "user_rps" is equal to the user's input of "Enter stop to end. Lets play rock, paper, scissors, please choose your weapon (Rock, Paper, or Scissors)"
    if user_rps.upper() == "STOP":  # If the user's input is stop
        break # game ends
    user_rps = user_rps.lower()  # players input is equal to the player's input in lowercase
    computer_rps = random.choice(moves) # computer_rps is equal to a random choice from the list of moves
    if user_rps not in valid_responses: # if user's input is not in the list of valid response 
        print("invalid try again") # print "invalid try again"

    else: # else
        if user_rps == computer_rps: # if user's input is equal to the computer's response
            print("It's a tie!") # print "It's a tie!"
        elif (user_rps == "rock"): # else if the user's input is rock
            if (computer_rps == "paper"): # if the computer's response is paper
                print("You lose") # the player loses
                cscore += 1 # add one to the computer's score
            elif (computer_rps == "scissors"): # else if the computers response is scissors
                print("You win") # the player wins
                pscore += 1 # add one to players score
        
        elif (user_rps == "paper"): # else if the user's input is paper
            if (computer_rps == "rock"): # if the computer's response is equal to rock
                print("You win!") # player wins
                pscore += 1 # add one to players score
            elif (computer_rps == "scissors"): # else if the the computer's response is equal to scissors
                print("You lose!") # Computer wins
                cscore += 1 # add one to computers score
            
        elif (user_rps == "scissors"): # else if player's input is equal to scissors
            if (computer_rps == "rock"): # if the computer's response is equal to rock
                print("You lose!") # computer wins
                cscore += 1 # add one to computers score
            if (computer_rps == "paper"): # if the computer's response is equal to paper
                print("You win") # player wins
                pscore += 1 # add one to players score
        
        print("Computer chose: " + computer_rps) # Always print the computer's response after telling whether the player won or not.

        while True: # creates loop
            csb = input("Would you like to see a scoreboard? (yes or no)") # csb is equal to the players input to the question "would you like to see a scoreboard"
            if csb.upper() == ("YES"): # if csb is equal to yes
                print("Player score is:", pscore) # print player scoreboard
                print("Computer score is", cscore) # print computer scoreboard
                break # Break and continue onto another round.
            elif csb.upper() == ("NO"): # else if csb is equal to no (uppercase or lowercase)
                break # break and play another round
            else: # if the player's input is anything besides yes or no
                print("invalid try again") # print "invalid try again".
 
        
    
       



  
