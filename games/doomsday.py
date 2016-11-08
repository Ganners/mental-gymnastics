import random
import datetime

class Doomsday:
    """Doomsday is a game which requires the doomsday rule to solve

    It will generate a random date and require the user to put down what
    day of the week that date will fall on
    """

    _name = "Doomsday Game"
    _question = "What day of the week would {0} fall on? (1 = Monday ... 7 = Sunday)"
    _date_format = "%d/%m/%Y"

    # Starts the game, returns a question string and validator function
    def play_game(self):
        """Returns a typle (string, func)

        The function returned will validate user input
        """

        # Pick a random date
        year, is_leap = self._random_year()
        month = self._random_month()
        day = self._random_day(is_leap, month)

        # Convert to a Python datetime
        date = datetime.date(year, month, day)
        correct_answer = date.weekday()

        # Generate question title
        question = self._question.format(date.strftime(self._date_format))

        # Create a validator
        def validator(answer):
            try:
                # Shift the correct answer up so 1 becomes a Monday
                return int(answer) == correct_answer + 1
            except ValueError:
                # Couldn't convert to int, just return false
                return False

        return question, validator

    # Get the name of the game
    @property
    def name(self):
        """Returns the name of the game"""
        return self._name

    def _random_year(self):
        """Returns a random year between 1900 and 2099"""
        year = random.randrange(1900, 2100)
        is_leap = self._is_leap(year)

        return year, is_leap

    def _random_month(self):
        """Returns a random month"""
        return random.randrange(1, 13)

    def _random_day(self, is_leap, month):
        """Returns a random day for a given month and potential leap year"""
        days_in_month = 31

        if month in [4, 6, 9, 11]:
            days_in_month = 30
        if month == 2:
            if is_leap:
                days_in_month = 29
            else:
                days_in_month = 28

        return random.randrange(1, days_in_month + 1)

    def _is_leap(self, year):
        """Returns True or False if year is a leap year"""
        return (year % 4) == 0

