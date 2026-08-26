import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
lives = 6
stages = hangman_art.stages
chosen_word = random.choice(word_list)
placeholder = ""

print(hangman_art.logo)
print(chosen_word)
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

correct_letters = []
guesses = []
game_over = False

print("Word to guess: " + placeholder)

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print("You already guessed that letter")
    guesses.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print("You guessed " + guess + " that's not in the word. You lose a life")
        if lives == 0:
            game_over = True

            print("IT WAS " + chosen_word + "!")
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
