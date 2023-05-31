# Christopher L'Helias
# 2/29/23
# Description:
# This will act as a magic 8 ball. It will ask the user what their question is. It will then provide a random response. 
# It will also keep track of how frequently each response is used. After answering the user's question, 
# it will ask whether or not the user wants to see how frequently each response has been used. 
# If the user responds "yes" a list of each response and how many times they have been used will pop up. 
# If the user's response is no, it will continue asking the user what their question is.
# Bugs: 
# If the user does respond with a actual question, the 8 ball will still give a response. 
# If a user doesn't respond with yes or no to whether or not they want to see the frequency, the 8 ball will just continue.
# Challenge:
# The 8 ball will ask the user if they want to see how frequently each response has been used, 
# then will display a chart with each response and how many times it has been used,
#  if the user's answer is yes. If the user's answer is no, the cycle will continue.
# Sources: none
import random # imports random, which allows functions to generate random numbers/values
responses = { # The possible responses to the users questions
    "Yes": 0, # "Yes" is a possible response to the users question, and how frequently this response has been used always starts off at zero
    "No": 0, # "No" is a possible response to the users question, and how frequently this response has been used always starts off at zero
    "Maybe": 0, # "Maybe" is a possible response to the users question, and how frequently this response has been used always starts off at zero
    "Ask Again Later": 0 # "Ask Again Later" is a possible response to the users question, and how frequently this response has been used always starts off at zero
}
print("To quit type stop")

while True: # Creates infinite loop
    
    answer = input("What is your question?") # The question the user asks is defined as the answer to the intial question.
    if (answer.upper() == "STOP"): # If the user's answer is stop
        break # While loop breaks 
    else:
        response = random.choice(list(responses.keys())) # response is equal to a random choice from the list of responses
        responses[response] += 1 # Add 1 to the number of times the selected response was used
        print(response) # print a response

        frequency = input("Would you like to see how frequently each asnwer has been given") # The user's answer to the question "Woudld you like to see how frequently each asnwer has been given" is defined as frequency.
    if frequency.upper() == "YES": # if the users answer is yes
        print("Here is how frequently each response was given") # print "here is how frequently each response was given"
        for response, frequency in responses.items():# for the response
            print(f"{response}: {frequency}") # print each response and how frequently it has been used
    elif frequency.upper() == "NO": # else if users answer is no 
        continue # continue the cycle and ask what the users question is

   

