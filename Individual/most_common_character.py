from collections import Counter


def main():
    string = input("String:")
    most_common_char = most_common_character(str)
    print(f"The most common character is: {most_common_char}")


def most_common_character(string):
    counter = Counter(string)
    max_occurence = max(counter.values())
    most_common = []
    for k,v in counter.items():
        if v == max_occurence:
            most_common += k
    return most_common[0]


if __name__ == "__main__":
    main()