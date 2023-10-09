def main():
    user_input = input("Please input text: ")
    twttr(user_input)
    print()

def twttr(string):
    for i in string:
        if i.upper() not in ["A", "E", "I", "O", "U"]:
            print(i, end="")
main()