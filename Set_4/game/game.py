import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

nr = random.randint(1, level)

while True:
    try:
        n = int(input("Guess: "))
        if n > 0:
            if n > nr:
                print ("Too large!")
            elif n < nr:
                print ("Too small!")
            else:
                print ("Just right!")
                break
    except ValueError:
        pass
