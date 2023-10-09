def main():
    user_time = input ("What time is it? ").strip().casefold()
    time_f = convert(user_time)
    if 7 <= time_f <= 8:
        print ("breakfast time")
    elif 12 <= time_f <= 13:
        print ("lunch time")
    elif 18 <= time_f <= 19:
        print ("dinner time")

def convert(time):
    if "p.m." in time or "pm" in time:
        time = time.rstrip("p.m.")
        hours, minutes = time.split (":")
        time_as_float = (float(hours) + 12) + (float(minutes) / 60)
        return time_as_float
    else:
        time = time.rstrip("a.m.")
        hours, minutes = time.split (":")
        time_as_float = (float(hours)) + (float(minutes) / 60)
        return time_as_float

if __name__ == "__main__":
    main()
