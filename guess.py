#Guess the number
import random
print("Welcome!You have to guess a number between 1 and 10.")
while True:
    try:
        yourchoice = int(input("Enter your choice: "))
        compchoice = random.randint(1, 10)
        if compchoice == yourchoice:
            print(f"Computer also chose {compchoice}! You win!")
            break  # Exit the loop because the user won
        else:
            print(f"Computer chose {compchoice}. You Lose! Try Again.")
    except ValueError:
        print("Please enter a number between 1 and 10.")
