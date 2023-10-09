#import emoji library
import emoji

# ask user for input
def main():
    convert_to_emoji(user_input("Input: "))

def user_input(prompt):
    return input(prompt)

# convert user input into emoji and print
def convert_to_emoji(userinput):
    print ("Output: " + emoji.emojize(userinput, language='alias'))

if __name__ == "__main__":
    main()

