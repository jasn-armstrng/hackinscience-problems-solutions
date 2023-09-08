import datetime


def friday_13th():
    # Start from today in case today's Friday 13th
    date = datetime.date.today()

    # Weekday() function returns the day of the week as an integer (Monday is 0, Sunday is 6)
    # So Friday is 4

    # Loop until find the next Friday 13th
    while True:
        if date.day == 13 and date.weekday() == 4:
            break
        date += datetime.timedelta(days=1)

    return date.strftime("%Y-%m-%d")


def main() -> None:
    print(friday_13th())


if __name__ ==  "__main__":
    main()
