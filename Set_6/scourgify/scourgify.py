import sys
import csv

# main function
def main():
    students = check_cmd_line_arg()
    write_list(students)

#check if only two command-line arguments
def check_cmd_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line argumets")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
#check if command-line argument is CSV file
    else:
         if sys.argv[1].strip().endswith(".csv") == True or sys.argv[2].strip().endswith(".csv") == True:
            try:
                students = []
                with open(sys.argv[1]) as file:
                    csv_reader = csv.DictReader(file)
                    for row in csv_reader:
                        last, first = row["name"].split(",")
                        students.append({"first" : first.strip() , "last" : last.strip() , "house" : row["house"]})
                    return students
            except FileNotFoundError:
                sys.exit("File does not exist")
         else:
             sys.exit("Not a CSV file")

#create output CSV file
def write_list(list):
    with open(sys.argv[2], "w") as file:
        csv_writer = csv.DictWriter(file, fieldnames = list[0].keys())
        csv_writer.writeheader()
        for row in list:
            csv_writer.writerow(row)


if __name__ == "__main__":
    main()






