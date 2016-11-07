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
    'seperator': '*' * 40,
    'starting_game': "Starting random game '{0}'",
    'submit_answer': "What is your answer?: ",
    'incorrect': "Sorry, that answer is incorrect. Please try again",
    'correct': "Congratulations, that answer is correct",
}

# How many correct answers are required to win?
correct_required = 1

def main():

    total_correct = 0

    while total_correct < correct_required:
        # Choosing a random game
        game = random.choice(games_registry)

        # Output the game
        print(lang['seperator'])
        print(lang['starting_game'].format(game.name))
        print(lang['seperator'] + os.linesep)

        # Get a question and validator function for the game
        question, validator = game.play_game()

        # Ask it
        print(question)

        # Loop until an answer is correct
        is_correct = False

        while is_correct == False:
            user_input = input(lang['submit_answer'])
            is_correct = validator(user_input)

            # If that's not correct, provide a message before looping
            if is_correct == False:
                print(lang['incorrect'])

        # That was correct
        print(lang['correct'])

        # Increment correct
        total_correct += 1

if __name__ == "__main__":
    main()
