import random

# ANSI color escape codes, used this side https://ask.replit.com/t/how-do-i-make-colored-text-in-python/29288 for generate colors in python
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
}

# List of colors
colors = list(color_codes.keys())

# Dictionary mapping color combinations to the resulting color
color_combinations = {
    ("red", "blue"): "purple",
    ("blue", "yellow"): "green",
    ("yellow", "red"): "orange",
    ("red", "green"): "brown",
    ("blue", "green"): "teal",
    ("yellow", "green"): "lime",
    ("red", "orange"): "maroon",
    ("yellow", "orange"): "amber",
    ("purple", "green"): "olive",
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
        return None  # Return None if the combination is not in the dictionary

def main():
    print("Welcome to the Color Mixing Game!")
    print("Try to guess the resulting color when you mix two colors.")

    play_again = 'y'
    total_score = 0  # Initialize total score
    while play_again.lower() == 'y':
        round_score = 0  # Initialize score for the current round
        # Pick two random colors
        color1 = random.choice(colors)
        color2 = random.choice(colors)

        # Ensure a valid color combination is selected
        while mix_colors(color1, color2) is None:
            color1 = random.choice(colors)
            color2 = random.choice(colors)

        # Determine the correct answer and two incorrect answers
        correct_answer = mix_colors(color1, color2)
        incorrect_answers = [color for color in colors if color != correct_answer]
        random.shuffle(incorrect_answers)
        options = [correct_answer] + incorrect_answers[:2]
        random.shuffle(options)

        print("You mix {} and {}...".format(color_codes[color1] + color1 + "\033[0m", color_codes[color2] + color2 + "\033[0m"))
        print("What color do you think you'll get?")
        for i, option in enumerate(options, 1):
            # Ensure option is a valid color
            if option in color_codes:
                print("{}. {}".format(i, color_codes[option] + option + "\033[0m"))

        # Allow the player to guess two times
        correct_guess = False
        for _ in range(2):
            choice = input("Enter your choice (1, 2, or 3): ")
            try:
                choice_index = int(choice) - 1
                user_guess = options[choice_index]
            except (ValueError, IndexError):
                print("Invalid choice! Please enter 1, 2, or 3.")
                continue

            if user_guess == correct_answer:
                print("Congratulations! You guessed it right. {} is the resulting color!".format(color_codes[correct_answer] + correct_answer + "\033[0m"))
                correct_guess = True
                round_score += 1  # Increment score for correct guess
                total_score += 1  # Increment total score
                break
            else:
                print("Sorry, that's not correct.")
        
        if not correct_guess:
            print("You've used all your guesses. The correct answer was {}.".format(color_codes[correct_answer] + correct_answer + "\033[0m"))
            print("Game Over!")
            break

        print("Your score for this round: {}".format(round_score))  # Display round score
        print("Your total score: {}".format(total_score))  # Display total score

        play_again = input("Do you want to play again? (y/n): ")

    print("Thank you for playing! See you soon!")

if __name__ == "__main__":
    main()