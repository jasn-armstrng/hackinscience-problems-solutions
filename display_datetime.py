from datetime import datetime


def main() -> None:
    now = datetime.now()
    print(f"Today is {now.date()} and it is {now.strftime('%H:%M:%S')}.")


if __name__ ==  "__main__":
    main()
