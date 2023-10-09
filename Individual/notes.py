from itertools import combinations_with_replacement


def main():
    notes = [10, 20, 50]
    new_counter = 0
    for i in range(10):
        for j in combinations_with_replacement(notes, i+1):
            if sum(j) == 100:
                new_counter += 1
                print(j)
    print(f"number of pairs = {new_counter}")

if __name__ == "__main__":
    main()



#def main():
#    notes = [10, 20, 50]
#    new_counter = 0
#    new_pairs = []
#    for i in range(10):
#        for j in range(3 ** (i+1)):
#            combination = []
#            k = j
#            for _ in range(i+1):
#                combination.append(notes[k % 3])
#                k //= 3
#            if sum(combination) == 100 and all(combination[j] >= combination[j+1] for j in range(len(combination)-1)):
#                new_counter += 1
#                new_pairs.append(combination)
#    print(f"number of pairs = {new_counter}")
#    print(*new_pairs, sep="\n")
#
# if __name__ == "__main__":
#    main()
