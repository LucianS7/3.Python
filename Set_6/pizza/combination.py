import itertools


notes = [50, 20, 10]
result = []
for i in range(1, 11):
    for combination in itertools.combinations_with_replacement(notes, i):
        if sum(combination) == 100:
            result.append(combination)
print(len(result))