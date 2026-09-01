import art
print(art.logo)

continue_auction = True
auction_data = {}

while continue_auction == True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction_data[name] = bid
    another_bid = input("Are there any others bidders? Type 'yes' or 'no': ").lower()
    if another_bid == "yes":
        continue_auction = True
        print("\n" * 20)
    elif another_bid == "no":
        continue_auction = False
    else:
        print("Invalid input. Try again.")
        continue
def find_winner():
    max_value = 0
    name_winner = ""
    for key in auction_data:
        if max_value < auction_data[key]:
            max_value = auction_data[key]
            name_winner = key
    return name_winner, max_value
name_winner, max_value = find_winner()
print(f"The winner is {name_winner} with a bid of ${max_value}")