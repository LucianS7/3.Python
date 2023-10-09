import sys
from datetime import datetime,date
import inflect


def main():
    age_in_min = age_in_minutes(get_date_of_birth(input("Date of birth: ")))
    p = inflect.engine()
    print(f"{p.number_to_words(age_in_min, andword='').capitalize()} minutes")


def get_date_of_birth(dob):
    try:
        date_of_birth = datetime.strptime(dob, "%d/%m/%Y").date()
        if date_of_birth < date.today():
            return date_of_birth
        else:
            sys.exit("Invalid date of birth")
    except ValueError:
        sys.exit("Invalid date of birth")


def age_in_minutes(date_of_birth):
    today = date.today()
    age = today - date_of_birth
    age_in_minutes = int(age.days * 60 * 24)
    return age_in_minutes


if __name__ == "__main__":
    main()


