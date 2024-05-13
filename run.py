import random
from colors import color_codes, MAX_TRIES


#ANSI color escape codes
color_codes = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    "teal": "\033[96m",
    "white": "\033[97m",
    "orange": "\033[38;5;208m",  # Orange color
    "maroon": "\033[38;5;88m",   # Maroon color
    "olive": "\033[38;5;58m",    # Olive color
    "navy": "\033[38;5;21m",     # Navy color
    "forest green": "\033[38;5;28m",  # Forest Green color
    "burnt umber": "\033[38;5;88m",   # Burnt Umber color
    "burnt sienna": "\033[38;5;130m", # Burnt Sienna color
    "goldenrod": "\033[38;5;136m",    # Goldenrod color
    "amber": "\033[38;5;202m"         # Amber color
}

def mix_colors(color1, color2):
    """
    Function to mix two colors and return the resulting color.
    """
    # Sort the colors to handle different orderings
    colors = tuple(sorted([color1, color2]))
    if colors in color_combinations:
        return color_combinations[colors]
    else:
        return "Sorry, I don't know what color you get by mixing {} and {}.".format(color1, color2)
