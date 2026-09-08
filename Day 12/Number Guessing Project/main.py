import art
import random
random_number = random.randint(1,100)
print(art.logo)

print("Welcome to Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()

def choose_number(attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")

def check_number(attempts):
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess > random_number:
            print("too High.\nGuess Again: ")
            attempts -= 1
            choose_number(attempts)
        elif guess < random_number:
            print("too Low.\nGuess Again: ")
            attempts -= 1
            choose_number(attempts)
        else:
            print(f"You got it! The number I was thinking of was {random_number}." )
            break
    else:
        print(f"You've run out of guesses. The number was {random_number}.")

if difficulty == "easy":
    attempts = 10
    choose_number(attempts)
    check_number(attempts)
elif difficulty == "hard":
    attempts = 5
    choose_number(attempts)
    check_number(attempts)
else:
    print("Please type 'easy' or 'hard'.")