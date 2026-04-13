class Card():
    SUITES = ['HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']

    def __init__(self, suite, rank):
        if not isinstance(suite, str):
            raise TypeError(f"Suite must be a string. Got {type(suite).__name__} instead.")
        if not isinstance(rank, str):
            raise TypeError(f"Rank must be a string. Got {type(rank).__name__} instead.")
        
        suite_upper = suite.upper()
        rank_upper = rank.upper()

        if suite_upper not in self.SUITES:
            raise ValueError(f"Invalid suite '{suite}'. Accepted suites are: {', '.join(self.SUITES)}.")
        if rank_upper not in self.RANKS:
            raise ValueError(f"Invalid rank '{rank}'. Accepted ranks are: {', '.join(self.RANKS)}.")

        self.suite = suite_upper
        self.rank = rank_upper

    def print_card(self):
        print(f"{self.rank} of {self.suite}")

if __name__ == "__main__":
    card1 = Card("Hearts", "Ace")
    card2 = Card("Spades", "10")
    card3 = Card("Diamonds", "Queen")
    try:
        invalid_card = Card("Stars", "11")
        invalid_card.print_card()
    except ValueError as e:
        print(e)

    card1.print_card()  # Output: ACE of HEARTS
    card2.print_card()  # Output: 10 of SPADES
    card3.print_card()  # Output: QUEEN of DIAMONDS