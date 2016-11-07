from games.doomsday import Doomsday
from unittest import TestCase

class TestDoomsday(TestCase):

    doomsday = Doomsday()

    def test_play_game(self):
        """Test that everything gets called as we expect, and validates correctly"""
        doomsday = Doomsday()

        # Mock return values from the randomizers
        doomsday._random_year = lambda: (2016, True)
        doomsday._random_month = lambda: 3
        doomsday._random_day = lambda is_leap, month: 16

        question, validator = doomsday.play_game()
        expected_answer = 3 # Wednesday
        self.assertTrue(validator(expected_answer))

    def _is_leap(self):
        self.assertTrue(self.doomsday._is_leap(2016))
        self.assertTrue(self.doomsday._is_leap(2020))
        self.assertFalse(self.doomsday._is_leap(2015))
        self.assertFalse(self.doomsday._is_leap(2019))

    # These tests all use randomisation, and so they lack determinism
    # but with enough iterations we can get a good coverage

    def test_random_year(self):
        for i in range(0, 1000):
            year, _ = self.doomsday._random_year()
            self.assertLessEqual(year, 2100)
            self.assertGreaterEqual(year, 1900)

    def test_random_month(self):
        for i in range(0, 100):
            month = self.doomsday._random_month()
            self.assertLessEqual(month, 12)
            self.assertGreaterEqual(month, 1)

    def test_random_day(self):
        for i in range(0, 100):
            day = self.doomsday._random_day(True, 2)
            self.assertLessEqual(day, 29)
            self.assertGreaterEqual(day, 1)

            day = self.doomsday._random_day(False, 2)
            self.assertLessEqual(day, 28)
            self.assertGreaterEqual(day, 1)

            day = self.doomsday._random_day(False, 4)
            self.assertLessEqual(day, 30)
            self.assertGreaterEqual(day, 1)

            day = self.doomsday._random_day(False, 5)
            self.assertLessEqual(day, 31)
            self.assertGreaterEqual(day, 1)

if __name__ == '__main__':
    unittest.main()

