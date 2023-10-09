import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if w_hours := re.search(r"^(\d?\d):?([0-5]\d)? (AM|PM) to (\d?\d):?([0-5]\d)? (AM|PM)$", s.strip()):
        if 0 <= int(w_hours.group(1)) <= 12 and 0 <= int(w_hours.group(4)) <= 12:
            time_1 = time_format(w_hours.group(1), w_hours.group(2),w_hours.group(3))
            time_2 = time_format(w_hours.group(4), w_hours.group(5),w_hours.group(6))
            return (f"{time_1} to {time_2}")
        else:
            raise ValueError
    else:
        raise ValueError


def time_format(h,m,ampm):
    if ampm == "PM":
        if int(h) == 12:
            h = 12
        else:
            h = int(h) + 12
    else:
        if int(h) == 12:
            h = 0
        else:
            h = int(h)
    if m == None:
        m = 0
    else:
        m = int(m)
    return (f"{h:02}:{m:02}")


if __name__ == "__main__":
    main()