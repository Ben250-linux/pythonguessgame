# Made by Ben Hughes and it is free use I don't really care about it I was bored and that is why I made it
import random
import sys
print("Welcome to the number guessing game!")
# Picks a random number between 1 and 100
answer = random.randint(1,100)
# Asks the user what number they think it is
userguess = int(input("Please enter the number you think it is (You have 3 lives left): "))
if userguess == answer:
    print("You did it!")
    sys.exit() # Stops the game once the condition is met
elif userguess > answer:
    print("You lost a life! The number is lower than that!")
elif userguess < answer:
    print("You lost a life! The number is higher than that!")
# Asks the user what number it is again and says they have 2 lives left
userguess = int(input("You have 2 lives left, what do you think the number is? "))
if userguess == answer:
    print("Second Times the charm! You did it!")
    sys.exit() # Stops the game once the condition is met
elif userguess > answer:
    print("You lost a life! The number is lower than that!")
elif userguess < answer:
    print("You lost a life! The number is higher than that!")
# Tells the user that this is their last life
userguess = int(input("You have 1 life left. Choose wisely: "))
if userguess == answer:
    print("Third times the charm! You got it!")
# Doesn't need the stop condition since this is the last guess
elif userguess > answer:
    print(f"You didn't get it. The number was lower than that! The number was: {answer}")
elif userguess < answer:
    print(f"You didn't get it. The number was higher than that! The number was: {answer}")
