def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    df = float(d.removeprefix('$'))
    return df


def percent_to_float(p):
    pf = float (p.removesuffix('%')) / 100
    return pf


main()