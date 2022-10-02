import random
from tkinter import N

x = 0
limit = 10
guess = limit
play = True

print("\nWelcome to the number guessing game! \n")

while play == True : 
 randomint = random.randint(1,100) # In this case the range is from 1 to 100
 while guess > 0 :
    x = int(input("Enter a number between 1 and 100: "))
    if x > randomint:
         guess -= 1
         print("\nToo high!\n \nYou have " + str(guess) + " guesses left. ")
    elif x < randomint:
         guess -= 1
         print("\nToo low!\n \nYou have " + str(guess) + " guesses left. ")
    elif x == randomint:
         guess -= 1
         print("\nYou have guessed the correct number in " + str(limit - guess) + " guesses! \nCongratulations!\n")
         play = False
         #guess = limit
        # play = bool(input("Would you like to play again? (Y/N) "))
         #if play == False :
           #print("Thanks for playing!")
           #break
 else:
     print("\nGame over! The number was " + str(randomint) + ".\n")
     play = False
    #guess = limit
     #play = bool(input("Would you like to play again? (Y/N) "))
    # if play == False :
       # print("Thanks for playing!")
       # break

