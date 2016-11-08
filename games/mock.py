class MockGame:
    """Dumb mock implementation of a game"""

    _return_validator = lambda:  True
    _question = "Some Question"
    _name = "Mock Game"

    def play_game(self):
        """Returns a typle (string, func)

        The function returned will validate user input
        """
        return self._question, self._return_validator

    def set_validator(self, validator_func):
        """Set the validator return value"""
        self._return_validator = validator_func

    @property
    def name(self):
        return self._name

