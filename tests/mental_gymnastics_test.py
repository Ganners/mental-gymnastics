import mental_gymnastics
from unittest import TestCase
from unittest.mock import MagicMock
from games.mock import MockGame

class TestMain(TestCase):

    question_response = "Some Answer"
    mock_game = MockGame()

    def setUp(self):
        # Mock the game that will be played
        mental_gymnastics._choose_game = MagicMock()
        mental_gymnastics._choose_game.return_value = self.mock_game

        # Mock the response from asking a question
        mental_gymnastics._ask_question = MagicMock()
        mental_gymnastics._ask_question.return_value = self.question_response

        # Mock the validator on the MockGame
        self.mock_validator = MagicMock()
        self.mock_validator.return_value = True
        self.mock_game.set_validator(self.mock_validator)

    def tearDown(self):
        mental_gymnastics._choose_game.reset_mock()
        mental_gymnastics._ask_question.reset_mock()
        self.mock_validator.reset_mock()

    def test_can_finish(self):
        """Tests that with a passing game, everything runs once and finishes"""
        mental_gymnastics.default_correct_required = 1
        mental_gymnastics.main()

        # Make some assertions
        mental_gymnastics._choose_game.assert_called_once_with()
        mental_gymnastics._ask_question.assert_called_once_with(mental_gymnastics.lang['submit_answer'])
        self.mock_validator.assert_called_once_with(self.question_response)

    def test_can_repeat(self):
        """Tests that if we need 5 games to win, 5 games will play"""
        mental_gymnastics.default_correct_required = 5
        mental_gymnastics.main()

        # Make some assertions
        self.assertEqual(mental_gymnastics._choose_game.call_count, 5)
        self.assertEqual(mental_gymnastics._ask_question.call_count, 5)
        self.assertEqual(self.mock_validator.call_count, 5)

    def test_can_ask_many(self):
        """Tests that if we get it wrong constantly, we'll finish but hit a limit"""
        self.mock_validator.return_value = False
        mental_gymnastics.default_correct_required = 1
        mental_gymnastics.main()

        # We'll hit the retry limit
        self.assertEqual(mental_gymnastics._ask_question.call_count, mental_gymnastics.retry_limit)

    def test_get_correct_required(self):
        """Tests some options parsing"""

        # Empty should default
        args = "".split()
        self.assertEqual(mental_gymnastics._get_correct_required(args),
                         mental_gymnastics.default_correct_required)

        # -r should overwrite
        args = "-r 3".split()
        self.assertEqual(mental_gymnastics._get_correct_required(args), 3)

        # -r with invalid number should default
        args = "-r nope".split()
        self.assertEqual(mental_gymnastics._get_correct_required(args),
                         mental_gymnastics.default_correct_required)

        # --required should overwrite
        args = "--required 3".split()
        self.assertEqual(mental_gymnastics._get_correct_required(args), 3)

        # --required with invalid number should default
        args = "--required nope".split()
        self.assertEqual(mental_gymnastics._get_correct_required(args),
                         mental_gymnastics.default_correct_required)

if __name__ == '__main__':
    unittest.main()

