import string

def main():
    str1 = input("Enter first string:")
    str2 = input("Enter second string:")
    is_anagram = are_anagrams(str1, str2)
    if is_anagram:
        print("The given strings are anagrams")
    else:
        print("The given strings are not anagrams")


def are_anagrams(s1,s2):
    s1 = s1.strip().lower()
    s2 = s2.strip().lower()
    punctuation = string.punctuation + " "
    char_list1 = "".join(c for c in s1 if c not in punctuation)
    char_list2 = "".join(c for c in s2 if c not in punctuation)
    return sorted(char_list1) == sorted(char_list2)


if __name__ == "__main__":
    main()

