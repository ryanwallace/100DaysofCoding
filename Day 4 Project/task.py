import random
import pictures

print("Welcome to rock paper scissors!!")

game_over = False

while not game_over:
    computer = random.randint(0, 2)

    player = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
    if player >= 0 and player <= 2:
        print(pictures.pics[player])

    print("Computer chose:")
    print(pictures.pics[computer])

    if player <= 0 or player >= 3:
        print("Invalid entry. You lose!")
    elif player == 0 and computer == 1:
        print("You lose!")
    elif player == 0 and computer == 2:
        print("You win!")
    elif player == 1 and computer == 0:
        print("You win!")
    elif player == 1 and computer == 2:
        print("You lose!")
    elif player == 2 and computer == 0:
        print("You lose!")
    elif player == 2 and computer == 1:
        print("You win!")
    else:
        print("It's a draw!")

    play_again = (input("Would you like to play again? Type 'y' or 'n': ").
                  lower())
    if play_again == "n":
        game_over = True

print("\nThank you for playing!!!")
