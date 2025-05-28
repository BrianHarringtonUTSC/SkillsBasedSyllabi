#prompt the trainer for the passcode
passcode = input("Trainer: enter 5 letter passcode: ")
#print a bunch of empty lines so that the entered passcode scrolls off the screen
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
####ROUND 1#####
print("Round 1: Guess 5 letters to see if they're in the passcode ")
#do this 5 times... later when we learn about loops, we can come back and make
#this a lot simpler
guess_1 = input("Guess #1: letter to check: ")
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
position_guess_1 = input("Guess #1: position to check: ")
position_guess_1 = int(position_guess_1)
print(passcode[position_guess_1] == letter_guess_1)

letter_guess_2 = input("Guess #2: letter to check: ")
position_guess_2 = input("Guess #2: position to check: ")
position_guess_2 = int(position_guess_1)
print(passcode[position_guess_2] == letter_guess_2)

letter_guess_3 = input("Guess #3: letter to check: ")
position_guess_3 = input("Guess #3: position to check: ")
position_guess_3 = int(position_guess_3)
print(passcode[position_guess_3] == letter_guess_3)

letter_guess_4 = input("Guess #4: letter to check: ")
position_guess_4 = input("Guess #4: position to check: ")
position_guess_4 = int(position_guess_4)
print(passcode[position_guess_4] == letter_guess_4)

letter_guess_5 = input("Guess #5: letter to check: ")
position_guess_5 = input("Guess #5: position to check: ")
position_guess_5 = int(position_guess_5)
print(passcode[position_guess_5] == letter_guess_5)


#####ROUND 3#####
print("Round 3: Guess the whole word, and I'll tell you if it's correct")
guess = input("Guess #1: guess the passcode: ")
print(guess == passcode)

guess = input("Guess #2: guess the passcode: ")
print(guess == passcode)

guess = input("Guess #3: guess the passcode: ")
print(guess == passcode)

guess = input("Guess #4: guess the passcode: ")
print(guess == passcode)

guess = input("Guess #5: guess the passcode: ")
print(guess == passcode)
