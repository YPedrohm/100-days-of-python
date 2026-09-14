import art
import random
from game_data import data
import os

print(art.logo)

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name} a {account_description} from {account_country}"

def check_followers(first, second, choice):
    if choice == "a":
        return first["follower_count"] > second["follower_count"]
    elif choice == "b":
        return second["follower_count"] > first["follower_count"]
    return False

def compare(compare_a, compare_b):
    print("Compare A: " + format_data(compare_a))
    print(art.vs)
    print("Compare B: " + format_data(compare_b))

def select_random_account():
    first_account = random.choice(data)
    second_account = random.choice(data)

    while second_account == first_account:
        second_account = random.choice(data)

    compare(first_account, second_account)
    return first_account, second_account

score = 0

first_account, second_account = select_random_account()
choice = input("Who has more followers? Type 'A' or 'B': ").lower()
right_answer = check_followers(first=first_account, second=second_account, choice=choice)

while right_answer:
    score += 1

    first_account = second_account
    second_account = random.choice(data)
    while second_account == first_account:
        second_account = random.choice(data)

    os.system("cls")
    print(art.logo)
    print(f"You're right! Current score: {score}")
    compare(first_account, second_account)

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    right_answer = check_followers(first=first_account, second=second_account, choice=choice)


print(f"Sorry, that's wrong. Final Score: {score}")