import argparse


def main():
    parser = argparse.ArgumentParser(description="maximum from a list of numbers")
    parser.add_argument("-numbers", nargs="+", type=int, help="list of numbers")
    args=parser.parse_args()
    print(max(args.numbers))


if __name__ == "__main__":
    main()