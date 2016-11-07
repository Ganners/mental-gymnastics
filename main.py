#!/usr/bin/env python3

import os
import random

from games.doomsday import Doomsday

# Registry of games
games_registry = [
    Doomsday(),
]

# Language strings
lang = {
    'starting_game': " Starting random game: {0} ",
    'submit_answer': "What is your answer?: ",
    'incorrect': "Sorry, that answer is incorrect. Please try again ({0} attempts remaining)",
    'correct': "Congratulations, that answer is correct",
    'limit_reached': "You have reached the limit",
}

# How many correct answers are required to win?
correct_required = 1
retry_limit = 100

def main():

    total_correct = 0

    while total_correct < correct_required:
        # Choosing a random game
        game = _choose_game()

        # Output the game
        starting_game = lang['starting_game'].format(game.name)
        seperator = '*' * len(starting_game)
        print(seperator)
        print(starting_game)
        print(seperator + os.linesep)

        # Get a question and validator function for the game
        question, validator = game.play_game()

        # Ask it
        print(question)

        # Loop until an answer is correct
        is_correct = False
        total_incorrect = 0

        while is_correct == False and total_incorrect < retry_limit:
            user_input = _ask_question(lang['submit_answer'])
            is_correct = validator(user_input)

            # If that's not correct, provide a message before looping
            if is_correct == False:
                total_incorrect += 1
                remaining = retry_limit - total_incorrect
                print(lang['incorrect'].format(remaining))

        if is_correct == False:
            print(lang['limit_reached'])
            return # Must break out, probable infinite loop reached

        print(lang['correct'])
        total_correct += 1

def _choose_game():
    return random.choice(games_registry)

def _ask_question(question):
    return input(question)

if __name__ == "__main__":
    main()

