from common import Suits, Ranks

class Card:
    def __init__(self, suit, rank):
        self.suit: Suits = suit
        self.rank: Ranks = rank
        
    def get_value(self):
        return self.rank.get_value()
    
    def __repr__(self):
        return f"{self.suit.to_char()}{self.rank.to_char()}"