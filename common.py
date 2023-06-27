from enum import Enum

MAX_POINTS = 21



class Suits(Enum):
    def to_char(self):
        return self.name[0]
    
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4
    
class Ranks(Enum):
    def to_char(self):
        match self:
            case Ranks.ACE:
                return 'A'
            case Ranks.JACK:
                return 'J'
            case Ranks.QUEEN:
                return 'Q'
            case Ranks.KING:
                return 'K'
            case _:
                return self.value
            
    def get_value(self):
        match self:
            case Ranks.QUEEN:
                return 10
            case Ranks.KING:
                return 10
            case _:
                return self.value
        
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    JACK = 10
    QUEEN = 11
    KING = 12
    
class Action(Enum):
    STAND = 1
    HIT = 2
    DOUBLE = 3
    SPLIT = 4
    
class Result(Enum):
    LOSE = 1
    WIN = 2
    STANDOFF = 3