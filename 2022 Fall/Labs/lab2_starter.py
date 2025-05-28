#prompt the trainer for the passcode
passcode = input("Trainer: enter 5 letter passcode: ")
#print a bunch of empty lines so that the entered passcode scrolls off the screen
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
####ROUND 1#####
print("Round 1: Guess 5 letters to see if they're in the passcode ")
#do this 5 times... later when we learn about loops, we can come back and make
#this a lot simpler
guess_1 = input("Guess #1: letter to check: ")
#this will print True because the letter a is in the word apple
print(guess_1 in passcode)

guess_2 = input("Guess #2: letter to check: ")
print(guess_2 in passcode)

guess_3 = input("Guess #3: letter to check: ")
print(guess_3 in passcode)

guess_4 = input("Guess #4: letter to check: ")
print(guess_4 in passcode)

guess_5 = input("Guess #5: letter to check: ")
print(guess_5 in passcode)

#####ROUND 2#####
print("Round 2: Guess 5 letter/position combinations to see if you have them correct")
letter_guess_1 = input("Guess #1: letter to check: ")
position_guess_1 = int(input("Guess #1: position to check: "))
#this will print True, becuase the 0th character of apple is equal to 'a'
#remember that we start counting from 0
#and if you're wondering why we use == instead of just =, it's because
#we've already used = to mean (assign to a variable)
print(passcode[position_guess_1] == letter_guess_1)


#####ROUND 3#####
print("Round 3: Guess the whole word, and I'll tell you if it's correct")
guess = input("Guess #1: guess the passcode: ")
#this will print true because the two strings are equal
#but be careful, they have to be exactly equal
print(guess == passcode)



