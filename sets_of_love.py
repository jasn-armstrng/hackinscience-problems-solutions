alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'III']
bob = ['IV', 'III', 'III', 'XX', 'II', 'XX']
silvester = ['XVIII', 'XIX', 'III', 'I', 'III', 'XVIII']


def love_meet(bob, alice):
    return set(bob).intersection(alice)


def affair_meet(bob, alice, silvester):
    return set(alice).intersection(silvester).difference(bob)


def main() -> None:
    print(love_meet(bob, alice))
    print(affair_meet(bob, alice, silvester))


if __name__ == "__main__":
    main()
