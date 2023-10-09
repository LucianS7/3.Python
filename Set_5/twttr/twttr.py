def main():
    user_input = input("Input: ")
    print("Output: " + shorten(user_input))

def shorten(word):
    s_word = ""
    for i in word:
        if i.upper() not in ["A", "E", "I", "O", "U"]:
            s_word += i
    return s_word


if __name__ == "__main__":
    main()