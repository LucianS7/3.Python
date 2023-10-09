import sys
import csv
from tabulate import tabulate

#main function
def main():
    menu = check_if_csv()
    print(tab(menu))

#check if only one command-line argument
def check_if_csv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
# check if argument is a CSV file
    else:
        if sys.argv[1].strip().endswith(".csv") == False:
            sys.exit("Not a CSV file")
        else:
# check if file exists
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.reader(file)
                    menu = []
                    for row in reader:
                        menu.append(row)
                    return menu
            except FileNotFoundError:
                sys.exit("File does not exist")

#tabulate the pizza menu
def tab(menu):
     return tabulate(menu, headers = "firstrow", tablefmt = "grid")


if __name__ == "__main__":
    main()
