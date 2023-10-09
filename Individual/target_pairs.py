from itertools import combinations


def main():
    nr_list = get_list()
    sum_value = get_target_value()
    pairs = find_pairs(nr_list, sum_value)
    print (*pairs, sep="  ")


def get_list():
    while True:
        try:
            nr_str = input("Enter sequence the of numbers: ").strip()
            if nr_str == "":
                raise ValueError
            nr_list = [*map(int, nr_str.split(" "))]
        except ValueError:
            print("Invalid input. Please enter a non-empty sequence of integers")
            continue
        return nr_list


def get_target_value():
    while True:
        try:
            s_value = int(input("Enter target value: "))
        except ValueError:
            continue
        return s_value


def find_pairs(lst, s):
    pairs_list = []
    for x,y in combinations(lst,2):
        if x + y == s:
            pairs_list.append((x,y))
    return sorted(pairs_list, key=lambda x: x[0])


#def find_pairs(lst, s):
#    pairs_list = []
#    for i,x in enumerate(lst):
#        for y in lst[i+1:]:
#            if x + y == s:
#                pairs_list.append((x,y))
#    return sorted(pairs_list, key=lambda x: x[0])


if __name__ == "__main__":
    main()