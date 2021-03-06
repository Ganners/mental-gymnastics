import random
import datetime
from enum import Enum

class MathOperations(Enum):
    """Valid operaitons for the Math game"""
    multiplication = 1

class Math:
    """Math is a game which requires being able to multiply or divide numbers
    in your head

    It will generate a random pair of numbers to be multiply

    This may be altered in future to also include division, the interface will
    remain the same in such a case
    """

    _range_min = 10
    _range_max = 99

    _name = "Multiplication Challenge"
    _question = "What is {0} {1} {2}?"

    # Starts the game, returns a question string and validator function
    def play_game(self):
        """Returns a typle (string, func)

        The function returned will validate user input
        """

        # Generate two random numbers
        x = self._pick_number()
        y = self._pick_number()

        # Choose an operation
        operation = self._pick_math_operation()
        symbol = "?"
        correct_answer = 0

        # Set the symbol and answers
        if operation == MathOperations.multiplication:
            symbol = "x"
            correct_answer = self.multiply(x, y)

        # Generate question title
        question = self._question.format(x, symbol, y)

        # Create a validator
        def validator(answer):
            try:
                return int(answer) == correct_answer
            except ValueError:
                # Couldn't convert to int, just return false
                return False

        return question, validator

    # Get the name of the game
    @property
    def name(self):
        """Returns the name of the game"""
        return self._name

    def _pick_number(self):
        return random.randrange(self._range_min, self._range_max + 1)

    def _pick_math_operation(self):
        """Chooses an element from the enum MathOperation"""
        return random.choice(list(MathOperations))

    def multiply(self, x, y):
        """Bit of fun, multiplication without the use of the '*' or '/'."""

        if x == 0 or y == 0:
            return 0

        # Swap so that x becomes the smallest
        if x > y:
            y, x = x, y

        if x == 1:
            return y

        # Create a stack, avoid recursion
        stack = []

        while x > 1:
            stack.append(x)
            x >>= 1

        multiplied = y

        # Go through the stack, double the value accumulated so far.
        # If the value at the stack index is odd then add on the
        # largest number (y)
        for i in reversed(stack):
            multiplied <<= 1
            if (i & 1) == 1:
                multiplied += y

        return multiplied

