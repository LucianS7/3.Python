def main():
    answer = input("What's the answer to the Great Question of Life, the Universe and Everything? ").casefold().strip()
    if is_correct(answer):
        print("Yes")
    else:
        print ("No")

def is_correct(arg):
    return arg == "42" or arg == "forty-two" or arg == "forty two"

main()