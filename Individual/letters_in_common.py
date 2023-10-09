from itertools import combinations


def main():
    words = get_words()
    pairs = find_pairs_w_largest_nr_of_common_letters(words)
    for i in pairs:
        print (*i, sep=",")


def get_words():
    while True:
        words_str = input("Enter the words: ").strip().lower()
        words_list = words_str.split(" ")
        if len(words_list) >= 3:
            break
        else:
            print ("Enter at least 3 words")
            continue
    return words_list


def find_pairs_w_largest_nr_of_common_letters(words):
    pairs = []
    max_number_common_letters = 0
    for w1, w2 in combinations(words, 2):
        common_letters = set(w1) & set(w2)
        print(common_letters)
        if len(common_letters) > max_number_common_letters:
            max_number_common_letters = len(common_letters)
            pairs = [(w1,w2)]
        elif len(common_letters) == max_number_common_letters:
            pairs.append((w1,w2))
    return pairs


if __name__ == "__main__":
    main()
