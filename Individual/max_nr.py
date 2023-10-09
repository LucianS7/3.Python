import sys


def main():
    try:
        if len(sys.argv) > 1:
            args = sys.argv[1:]
            nr_list = [int(_) for _ in args]
            print(f"Largest number in the given sequence is: {max(nr_list)}")
        else:
            sys.exit("Too few command line arguments")
    except ValueError:
        sys.exit("Invalid command line arguments")


if __name__ == "__main__":
    main()

