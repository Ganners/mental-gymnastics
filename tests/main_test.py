import main
from unittest import TestCase
from unittest.mock import MagicMock
from games.mock import MockGame

class TestMain(TestCase):

    question_response = "Some Answer"
    mock_game = MockGame()

    def setUp(self):
        # Mock the game that will be played
        main._choose_game = MagicMock()
        main._choose_game.return_value = self.mock_game

        # Mock the response from asking a question
        main._ask_question = MagicMock()
        main._ask_question.return_value = self.question_response

        # Mock the validator on the MockGame
        self.mock_validator = MagicMock()
        self.mock_validator.return_value = True
        self.mock_game.set_validator(self.mock_validator)

    def tearDown(self):
        main._choose_game.reset_mock()
        main._ask_question.reset_mock()
        self.mock_validator.reset_mock()

    def test_can_finish(self):
        """Tests that with a passing game, everything runs once and finishes"""
        main.correct_required = 1
        main.main()

        # Make some assertions
        main._choose_game.assert_called_once_with()
        main._ask_question.assert_called_once_with(main.lang['submit_answer'])
        self.mock_validator.assert_called_once_with(self.question_response)

    def test_can_repeat(self):
        """Tests that if we need 5 games to win, 5 games will play"""
        main.correct_required = 5
        main.main()

        # Make some assertions
        self.assertEqual(main._choose_game.call_count, 5)
        self.assertEqual(main._ask_question.call_count, 5)
        self.assertEqual(self.mock_validator.call_count, 5)

    def test_can_ask_many(self):
        """Tests that if we get it wrong constantly, we'll finish but hit a limit"""
        self.mock_validator.return_value = False
        main.correct_required = 1
        main.main()

        # We'll hit the retry limit
        self.assertEqual(main._ask_question.call_count, main.retry_limit)

if __name__ == '__main__':
    unittest.main()

