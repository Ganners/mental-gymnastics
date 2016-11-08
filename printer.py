# List of ANSI escape sequence colors for foreground printing
colors = {
    'black': '0;30',
    'blue': '0;34',
    'green': '0;32',
    'cyan': '0;36',
    'red': '0;31',
    'purple': '0;35',
    'brown': '0;33',
    'yellow': '1;33',
    'white': '1;37',
    'dark_gray': '1;30',
    'light_blue': '1;34',
    'light_green': '1;32',
    'light_cyan': '1;36',
    'light_red': '1;31',
    'light_purple': '1;35',
    'light_gray': '0;37',
}

# The escape sequence for using a color
layout = '\033[{0}m'

# Utility functions for common colors

def red(string):
    _print_string(string, 'red', True)

def green(string):
    _print_string(string, 'green', True)

def blue(string):
    _print_string(string, 'blue', True)

def cyan(string):
    _print_string(string, 'cyan', True)

def _print_string(string, color, do_print = False):
    """Returns a string which will print to the terminal

    if do_print is True then it will trigger the builtin print
    """
    string = layout.format(colors[color]) + string + layout.format('0')

    if do_print:
        print(string)

    return string

