Mental Gymnastics
=================

The purpose of this application is that whenever a new terminal session is
created (which is fairly often for me), it will start a question (or series of)
that must be passed in order to continue.

Game types
----------

One of the following might be randomly chosen:

 + [x] What day of the week would x fall on
 + [x] What is the answer to x * y
 + [x] What is the answer to x / y
 + [ ] What year was x born
 + [ ] Who is the author of x

Intention
---------

This is intended to be run in your `.bashrc` (or `.zshrc`, `.profile` etc.) and
so will start when a session is created.

This might go something like:

 > git clone git@github.com:Ganners/mental-gymnastics.git

 > cd mental-gymnastics

 > echo "# Start mental gymnastics game when session starts\npython ${PWD}/main.py" >> $HOME/.zshrc

Interface
---------

A game should look like this:

```python
class ExampleGame:
    """Returns a question string and a validator function

    The validator function returns a bool
    """
    def play_game(self):
        # Randomly pick something to ask
        random_question = "this is some random question"
        random_answer = 5

        def validate(string_input):
            return int(string_input) == random_answer

        return (random_question, validate)

    @property
    def name(self):
        """Returns the name of the game to be used in strings"""
        return "This is the name of the game"
```

The class will have a `play_game` function which will return a string (the
question) and a function to validate an answer that must return a bool.
