# https://www.hackinscience.org/exercises/the-missing-card
# Define all the possible keys
keys: list = [
    "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S00", "SJ", "SQ", "SK", "SA",
    "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H00", "HJ", "HQ", "HK", "HA",
    "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D00", "DJ", "DQ", "DK", "DA",
    "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C00", "CJ", "CQ", "CK", "CA"
]

card_dict: dict = {key: 0 for key in keys}

def missing_card(cards: str) -> str:
    full_deck = {
        'S2': 0, 'S3': 0, 'S4': 0, 'S5': 0, 'S6': 0, 'S7': 0, 'S8': 0, 'S9': 0, 'S10': 0, 'SJ': 0, 'SQ': 0, 'SK': 0, 'SA': 0,
        'H2': 0, 'H3': 0, 'H4': 0, 'H5': 0, 'H6': 0, 'H7': 0, 'H8': 0, 'H9': 0, 'H10': 0, 'HJ': 0, 'HQ': 0, 'HK': 0, 'HA': 0,
        'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0, 'D6': 0, 'D7': 0, 'D8': 0, 'D9': 0, 'D10': 0, 'DJ': 0, 'DQ': 0, 'DK': 0, 'DA': 0,
        'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0, 'C7': 0, 'C8': 0, 'C9': 0, 'C10': 0, 'CJ': 0, 'CQ': 0, 'CK': 0, 'CA': 0}

    for card in cards.split():
        full_deck[card] = 1

    for key, value in full_deck.items():
          if value == 0:
              return key
    return "No card missing"

def main() -> None:
    #  print(card_dict)
    missing_card("S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK")

if __name__ == "__main__":
    main()
