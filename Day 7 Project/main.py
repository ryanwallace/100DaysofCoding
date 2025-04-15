import random
import hangman_art
from hangman_words import word_list

lives = 6
chosen_word = random.choice(word_list)

print(hangman_art.logo)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
wrong_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT******************"
          f"**********")
    guess = input("Guess a letter: ").lower()

    if guess not in correct_letters and guess not in wrong_letters:

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
                wrong_letters.append(guess)

        print("Word to guess: " + display)

        if guess not in chosen_word:
            print(f"'{guess}' is not in the word. You lose a life.")
            lives -= 1

            if lives == 0:
                game_over = True

                print(f"***********************YOU LOSE**********************")
                print(f"The correct answer was {chosen_word}.")

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN************************"
                  "****")

        print(hangman_art.stages[lives])

    else:
        print(f"You already guessed '{guess}'. Try again!")
