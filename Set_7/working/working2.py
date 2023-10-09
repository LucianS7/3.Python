import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if w_hours := re.search(r"^(\d?\d):?([0-5]\d)? (AM|PM) to (\d?\d):?([0-5]\d)? (AM|PM)$", s.strip()):
        if 0 <= int(w_hours.group(1)) <= 12 and 0 <= int(w_hours.group(4)) <= 12:
            if w_hours.group(3) == "PM":
                if int(w_hours.group(1)) == 12:
                    h_1 = 12
                else:
                    h_1 = int(w_hours.group(1)) +12
            else:
                if int(w_hours.group(1)) == 12:
                    h_1 = 0
                else:
                    h_1 = int(w_hours.group(1))
            if w_hours.group(6) == "PM":
                if int(w_hours.group(4)) == 12:
                    h_2 = 12
                else:
                    h_2 = int(w_hours.group(4)) + 12
            else:
                if int(w_hours.group(4)) == 12:
                    h_2 = 0
                else:
                    h_2 = int(w_hours.group(4))
            if w_hours.group(2) != None and w_hours.group(5) != None:
                min_1 = int(w_hours.group(2))
                min_2 = int(w_hours.group(5))
                return (f"{h_1:02}:{min_1:02} to {h_2:02}:{min_2:02}")
            else:
                if w_hours.group(2) == None and w_hours.group(5) == None:
                    return (f"{h_1:02}:00 to {h_2:02}:00")
                else:
                    raise ValueError
        else:
            raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()