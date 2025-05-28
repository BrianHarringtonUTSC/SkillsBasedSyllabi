#prompt the trainer for the passcode
passcode = input("Trainer: enter 5 letter passcode: ")
#print a bunch of empty lines so that the entered passcode scrolls off the screen
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
####ROUND 1#####
print("Round 1: Guess 5 letters to see if they're in the passcode ")
#do this 5 times... later when we learn about loops, we can come back and make
#this a lot simpler
guess_1 = input("Guess #1: letter to check: ")

#----DELETE THIS AND REPLACE WITH YOUR CODE----#
#this will print True because the letter a is in the word apple
print("A" in "Apple")
#----   ----#

#####ROUND 2#####
print("Round 2: Guess 5 letter/position combinations to see if you have them correct")
letter_guess_1 = input("Guess #1: letter to check: ")
position_guess_1 = input("Guess #1: position to check: ")
#this will print True, becuase the 0th character of apple is equal to 'a'
#remember that we start counting from 0
#and if you're wondering why we use == instead of just =, it's because
#we've already used = to mean (assign to a variable)


#----DELETE THIS AND REPLACE WITH YOUR CODE----#
#The line below will print True becuase A is the first letter of Apple
print("Apple"[0] == "A")
#The line below will print False because X is not the first letter of Ball
print("Ball"[0] == "X")
#----   ----#

#####ROUND 3#####
print("Round 3: Guess the whole word, and I'll tell you if it's correct")
guess = input("Guess #1: guess the passcode: ")
#this will print true because the two strings are equal
#but be careful, they have to be exactly equal
#----DELETE THIS AND REPLACE WITH YOUR CODE----#
#The line below will print True 
print("Apple" == "Apple")
#The line below will print False 
print("Ball" == "  bAll   ")
#----   ----#
