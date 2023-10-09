def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        date = input("Date: ").strip()
        try:
            month, day, year = date.split("/")
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            try:
                if "," in date:
                    month, day, year = date.split()
                    if month in months:
                        month = months.index(month) + 1
                    day = day.replace(",","")
                    if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                         break
            except:
                print()
                pass
    year = int(year)
    month = int(month)
    day = int(day)
    print (f"{year}-{month:02}-{day:02}")

main ()