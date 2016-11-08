from games.math import Math, MathOperations
from unittest import TestCase

class TestMath(TestCase):

    def test_play_game(self):
        math = Math()

        # Set a determinstic min and max
        math._range_min = 10
        math._range_max = 10

        # Set operation to multiplication
        math._pick_math_operation = lambda: MathOperations.multiplication

        question, validator = math.play_game()

        # Check question contains both numbers and is multiplication
        self.assertIn("10", question)
        self.assertIn("x", question)

        # Check the answer is 100 (as a string)
        self.assertTrue(validator("100"))
        self.assertFalse(validator("99"))

        # Repeat the test for division

        # Set operation to multiplication
        math._pick_math_operation = lambda: MathOperations.division

        question, validator = math.play_game()
        self.assertTrue(validator("1"))
        self.assertFalse(validator("10"))

