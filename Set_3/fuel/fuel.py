def main():
    user_input = input("Fuel level as fraction: ")
    converted_user_input = convert(user_input)
    output = gauge(converted_user_input)
    print (output)
def convert(fraction):
    while True:
        try:
            x, y = fraction.strip().split("/")
            x = int(x)
            y = int(y)
            f = x/y
            if x >=0 and y > 0 and x <= y:
                return round(f * 100)
            else:
                fraction = input ("Fuel level as fraction: ")
        except (ValueError, ZeroDivisionError):
            raise
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
if __name__ == "__main__":
    main()