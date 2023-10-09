def main():
    x = get_int("What's x? ")
    if x != None:
        print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        except EOFError:
            print()
            break

main ()
