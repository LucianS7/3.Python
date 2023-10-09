import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
font_list = figlet.getFonts()
cmd_arg_accepted_list = ["-f", "--font"]

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(font_list))
elif len(sys.argv) == 3 and sys.argv[1] in cmd_arg_accepted_list and sys.argv[2] in font_list:
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

user_input = input ("Input: ")
print(figlet.renderText(user_input))