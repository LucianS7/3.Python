import sys


def main():
    lines = check_cmd_line_arg()
    print (f"Number of lines of code = {lines_counter(lines)}")


#check if only one command-line argument
def check_cmd_line_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
# check if argument is a Python file
    else:
        if sys.argv[1].strip().endswith(".py") == False:
            sys.exit("Not a Python file")
        else:
# check if file exists
            try:
                with open(sys.argv[1]) as file:
                    lines=file.readlines()
                    return lines
            except FileNotFoundError:
                sys.exit("File does not exists")


#count the number of lines in the code
def lines_counter(lines):
    line_counter = 0
    for line in lines:
        if line.lstrip().startswith("#") == False and len(line.strip()) > 0:
            line_counter += 1
    return line_counter


if __name__ == "__main__":
    main()

