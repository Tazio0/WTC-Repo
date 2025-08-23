from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f_argument = random.choice(fonts)
    figlet.setFont(font = f_argument)

elif len(sys.argv) == 3:
    if sys.argv[1] != "-f":
        if sys.argv[1] != "--font":
            sys.exit("Invalid input, Try again")

    if sys.argv[2] in fonts:
        figlet.setFont(font = sys.argv[2])

    else:
        sys.exit("Invalid input, Try again")

else:
        sys.exit("Invalid input, Try again")


user_input = input("Input: ")

print(f"Output: {figlet.renderText(user_input)}")
