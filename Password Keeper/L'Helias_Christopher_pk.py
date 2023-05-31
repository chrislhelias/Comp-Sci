# Author: Christopher L'Helias
# Date: 4/14/23
# Description: This program will ask the user if they want to save their data for a certain website. If the user asnwer no then the computer will give the user some options, 
# one of which being to exit. If the user says yes the program will ask what the website is along with the corresponding password and username. All of this information is then 
# stored in three seperate lists. The user will then be asked what they would like to do out of 5 options - 1. See all entries, 2. Find specific entry, 3. Add another entry, 
# 4. Change username/password, 5. Exit." If the user chooses option 1, all of the websites, usernames, and passwords will print according to when they were entered, so they will 
# correspond with one another. If the user chooses option 2, the program will ask the user what website's information they would like to see. If the user's choice of website is 
# not in the list, the computer will say "Not here". If the user's choice of website is in the list, the corresponding username and password will print. If the user chooses option
# 3, the loop will break, so the user will once again be prompted with what website they would like to add. Thus, adding a new entry to the list. If the user chooses option 4, the program will 
# ask what website's password and username they would like to change. If the given website is not in the websites list, the program will print "Not here." If the user's choice of website is in 
# the websites list, the computer will find the username and password that corresponds and ask what the user would like to change them to. The program then will set the user's choices as the new 
# password and username for that website.
# Challenges: 
# The program allows the user to search for a specific websites data. 
# The program also allows the user to add new entries
# The program also allows the user to change a chosen website's username and password.
# Bugs: If the user enters the same website twice but different data, the program can only find the data for the first time the website was chosen.
# Source: None


websites = [] # Websites is equal to a list of websites that will be set by the user
user_names = [] # user_names is equal to a list of usernames that will be set by the user
passwords = [] # passwords is equal to a list of passwords that will be set by a user
while True: # Creates loop
    while True: # Creates loop
        keeper = input("Would you like to save your password and username for a certain website?") # Keeper is equal to the user's answer to the question "Would you like to save your password and username for a certain website?"
        keeper = keeper.lower() # Allow's the user's answer to be valid in uppercase or lowercase
    
        if keeper == "no": # If user's response is no
            break # break the second loop
        elif keeper == "yes": # Else if user's answer if yes
            ws = input("What is the website?") # The variable ws is equal to the user's answer to the question "what is the website?"
            un = input("What is your username?") # The variable un is equal to the user's answer to the question "what is your username?"
            ps = input("What is your password?") # The variable ps is equal to the user's input to the question "what is your password?"
            websites.append(ws) # Adds user's website to the list of websites
            user_names.append(un) # Adds user's username to the list of username
            passwords.append(ps) # Adds user's password to the list of passwords
        else: # If the user inputs anything besides yes or no
            print ("invalid try again") # Tell the user their input is invalid
        

    while True: # creates loop
        mode = input("What would you like to do? 1. See all entries, 2. Find specific entry, 3. Add another entry, 4. Change username/password, 5. Exit") # The variable mode is equal to the user's answer to the question "What would you like to do? 1. See all entries, 2. Find specific entry, 3. Add another entry, 4. Change username/password, 5. Exit."

        if mode == "5": # If user's input is equal to option 5 
            exit() # exit the program
        elif mode == "1": # else if user's input is equal to 1 
            for index in range(len(websites)): # Creates a sequence of numbers starting at 0 and going up to the amount in the websites list
                print("Website:", websites[index]) # Uses variable index to print out each website according to when they were entered in the websites list, so it will correspond with the following passwords and usernames.
                print("Username:", user_names[index]) # Uses variable index to print out each username according to when they were entered in the user_names list, so it will correspond with the following passwords and websites.
                print("Passwords:", passwords[index]) # Uses variable index to print out each passwords according to when they were entered in the passwords list, so it will correspond with the following usernames and websites.
        elif mode == "2": # else if user's input was option 2 
            web = input("What website would you like to see? ") # The variable web is equal to teh user's answer to the question "What website would you like to see?"
        
            if web not in websites: # If user's choice of website was not one he entered previously 
                print("Not here") # Print "Not here
            else: # else
                index = websites.index(web) # The variable index is equal to the first occurence of the user's website choice in the websites list
                print("Website:", websites[index]) # Prints the website the user chose
                print("Username:", user_names[index]) # Prints the username at the same index (corresponding)
                print("Passwords:", passwords[index]) # Prints the password at the same index (corresponding)
        elif mode == "3": # else if the user chooses option 3
            break # break which will allow the user to add more entries
        elif mode == "4": # else if the user chooses option 4 
            change = input("What websites username/password would you like to change") # The variable change is equal to the user's question "What website's username/password would you like to change?"
            if change not in websites: # if the user's choice of website is not in the list of websites 
                print("Not here") # Tell the user it is not in the list
            else: # else
                index = websites.index(change) # The variable index is equal to the index of the website the user chose within the website list.
                un = input("What is your new username?") # The variable un is equal to the user's answer to teh question "What is your new username?"
                ps = input("What is your new password?") # The variable ps is equal to the user's answer to the question "What is your new password?"
                passwords[index] = ps # Updates password
                user_names[index] = un # Updates username
                
        