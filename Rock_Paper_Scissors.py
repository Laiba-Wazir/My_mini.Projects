import random

def play_game():
    print("\n")
    print("==========ROCK PAPER SCISSOR GAME==========")
    print("This game is very famous nowadays\nIf you have not played this game, don't worry.\nHere are the rules for playing this game 😇 ")
    print("A rock beats scissors, scissors beat paper by cutting it, and paper beats rock by covering it.")
    
    youDict = {"r": 1, "p": -1, "s": 0}
    reverseDict = {1: "Rock", -1: "Paper", 0: "Scissor"}
    
    while True:
        computer = random.choice([1, -1, 0])
        youStr = input("\nEnter your choice ['r' for Rock, 'p' for Paper, 's' for Scissor]: ").lower()
        
        if youStr not in youDict:
            print("Invalid choice! Please choose again.")
            continue
        
        you = youDict[youStr]
        
        print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

        if computer == you:
            print("It's a Draw 😄")
        elif (you == 1 and computer == 0) or (you == -1 and computer == 1) or (you == 0 and computer == -1):
            print("You Win! 🥳🎉")
        else:
            print("You Lose! 🙁")
        
        choice = input("\nDo you want to play again (yes or no)? ").lower()
        if choice != "yes":
            print("Thanks for playing! Goodbye!")
            break

play_game()
