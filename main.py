import random
import game_data
import art


def random_key():
    random_key_one = random.randint(0, (len(game_data.data) - 1))
    return random_key_one


def choose_dict(key):
    new_player = game_data.data[key]
    return new_player


def format_string(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


continue_game = True
account_one = choose_dict(random_key())
account_two = choose_dict(random_key())
points = 0

while continue_game:
    print(art.logo)

    if points > 0:
        print(f"You are correct! You now have {points} points!")

    print(f"Compare A:", format_string(account_one))
    print(art.vs)
    print(f"Compare B:", format_string(account_two))

    question = input("Who has more followers? type 'A' or 'B': ").lower()
    if question == 'a' and account_one["follower_count"] >= account_two["follower_count"]:
        points += 1
    elif question == 'a' and account_one["follower_count"] < account_two["follower_count"]:
        print(f"Sorry that's wrong! Final score {points} points 😢😢")
        continue_game = False
    elif question == 'b' and account_one["follower_count"] <= account_two["follower_count"]:
        print("True")
        points += 1
    elif question == 'b' and account_one["follower_count"] > account_two["follower_count"]:
        print(f"Sorry that's wrong! Final score {points} points :(")
        continue_game = False
    else:
        print("Invalid input, try again!")

    account_one = account_two
    account_two = choose_dict(random_key())
