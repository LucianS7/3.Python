import random


def main():
    level = get_level()
    pr_c = 1
    correct_c = 0
    while pr_c <= 10:
        x  = generate_integer(level)
        y = generate_integer(level)
        error_c = 0
        while True:
            try:
                z = int(input(f"{x} + {y} = "))
                if z != x + y:
                    error_c += 1
                    if error_c == 3:
                        pr_c += 1
                        print(f"{x} + {y} = {x + y}")
                        break
                    elif error_c < 3:
                        print ("EEE")
                        pass
                else:
                    correct_c += 1
                    pr_c += 1
                    break
            except ValueError:
                error_c += 1
                if error_c == 3:
                    pr_c += 1
                    print(f"{x} + {y} = {x + y}")
                    break
                else:
                    print ("EEE")
                    pass
            except EOFError:
                pr_c = 11
                print()
                break

    print(f"Score: {correct_c}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2 ,3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()