import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

def deal_cards():
    for card in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))


def calculate_score():
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    user_aces = user_cards.count(11)
    computer_aces = computer_cards.count(11)

    while user_score > 21 and user_aces > 0:
        user_aces -= 1
        user_score -= 10
    while computer_score > 21 and computer_aces > 0:
        computer_aces -= 1
        computer_score -= 10
    return user_score, computer_score


def verify_champion(user_score, computer_score):
    user_blackjack = user_score == 21 and len(user_cards) == 2
    computer_blackjack = computer_score == 21 and len(computer_cards) == 2
    if user_score > 21:
        print("You went over. You lose!")
    elif user_blackjack and computer_blackjack:
        print("It's a tie!")
    elif user_blackjack:
        print("It's a Blackjack. You win!")
    elif computer_blackjack:
        print("Computer has Blackjack. You lose!")
    elif computer_score > 21:
        print("Computer went over. You win!")
    elif user_score > computer_score:
        print("You win!")
    elif user_score == computer_score:
        print("It's a tie!")
    else:
        print("You lose!")


def show_cards(user_score, computer_score):
    you_cards = ",".join(map(str, user_cards))
    print(f"Yours cards: [{you_cards}]. Current score: {user_score}")
    comp_cards = ",".join(map(str, computer_cards))
    print(f"Computer's cards: [{comp_cards}]. Current score: {computer_score}.")

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while play_game == "y":
    user_cards = []
    computer_cards = []
    print("\n" * 30)
    print(art.logo)
    deal_cards()
    user_score, computer_score = calculate_score()

    print(f"Your cards: [{user_cards[0]},{user_cards[1]}], current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 21:
        verify_champion(user_score, computer_score)

    while user_score < 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            user_cards.append(random.choice(cards))
            user_score, computer_score = calculate_score()
            if user_score >= 21:
                show_cards(user_score, computer_score)
                verify_champion(user_score, computer_score)
        else:
            while computer_score < 17:
                computer_cards.append(random.choice(cards))
                user_score, computer_score = calculate_score()
            show_cards(user_score, computer_score)
            verify_champion(user_score, computer_score)

    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()