from datetime import date
import sys
import inflect


def main():
    age_in_min = age_in_minutes(get_birth_date(input("Date of birth: ")))
    p = inflect.engine()
    print(f"{p.number_to_words(age_in_min, andword='').capitalize()} minutes")


def get_birth_date(s):
    try:
        date_of_birth = date.fromisoformat(s)
        if date_of_birth < date.today():
            return date_of_birth
        else:
            sys.exit("Invalid date")
    except ValueError:
        sys.exit("Invalid date")


def age_in_minutes(dob):
    today = date.today()
    age_in_min = int((today - dob).days) * 1440
    return age_in_min


if __name__ == "__main__":
    main()