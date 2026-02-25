import random
choices= ("scissors","paper","rock")
userchoice = input("Scissors paper or rock? ").lower()
compchoice = random.choice(choices)
if userchoice == compchoice:
    print(f"Comp chose {compchoice} Tie!")
elif userchoice == "scissors" and compchoice == "rock":
    print(f"Comp chose {compchoice} You Lose!")
elif userchoice == "scissors" and compchoice == "paper":
    print(f"Comp chose {compchoice} You Win!")
elif userchoice == "paper" and compchoice == "rock":
    print(f"Comp chose {compchoice} You win!")
