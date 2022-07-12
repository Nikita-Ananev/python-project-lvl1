"""Description of welcome."""


import prompt


def welcome_user():
    """Welcome function."""
    name = prompt.string('May I have your name?\n')
    print('Hello, {0}!'.format(name))
