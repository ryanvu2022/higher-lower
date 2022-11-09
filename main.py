from art import logo, vs
from game_data import data
import random


def get_info(item):
    """take the dictionary item and return an array of values"""
    value_array = []
    for value in item.values():
        value_array.append(value)
    return value_array


def compare(p1, p2):
    """compare the number of followers between 2 persons"""
    if p1[1] > p2[1]:
        return p1
    elif p1[1] < p2[1]:
        return p2


def play_game():
    """play the game"""
    print(logo)
    score = 0
    person1 = get_info(random.choice(data))

    game_continue = True
    while game_continue:
        person2 = get_info(random.choice(data))
        if person2 == person1:
            person2 = get_info(random.choice(data))

        print(f"Compare A: {person1[0]}, a {person1[2]}, from {person1[3]}")
        print(vs)
        print(f"Against B: {person2[0]}, a {person2[2]}, from {person2[3]}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if (guess == "a" and person1[1] < person2[1]) or (guess == "b" and person2[1] < person1[1]):
            print(f"Sorry, that's wrong. Final score: {score}")
            game_continue = False
        elif (guess == "a") or (guess == "b"):
            score += 1
            print(f"You're right! Current score: {score}")
            if guess == "b":
                person1 = person2
        else:
            print("Invalid input.")
            print(f"Final score: {score}")
            game_continue = False


play_game()
