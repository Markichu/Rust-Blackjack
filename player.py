from hand import Hand
from card import Card
from common import Action, Result
from collections import defaultdict

class Player():
    def __init__(self):
        self.hand: Hand = Hand()
        self.bet: int = 0
        self.balance: int = 0
        self.results: dict = {
            result: 0 for result in Result
        }
        self.initial_hand: str = "" 
        self.win_stats: dict = defaultdict(int)
        self.game_stats: dict = defaultdict(int)
        
    def place_bet(self):
        raise NotImplementedError()
        
    def run(self, dealer_card: Card):
        raise NotImplementedError()
        

class StandSoft17Player(Player):
    def place_bet(self):
        self.bet = 1
    
    def run(self, dealer_card: Card):
        if self.hand.get_value() >= 17:
            return Action.STAND
        return Action.HIT
        

class StandPlayer(Player):
    def place_bet(self):
        self.bet = 1
        
    def run(self, dealer_card: Card):
        return Action.STAND
    
class TestPlayer(Player):
    def place_bet(self):
        self.bet = 1
        
    def run(self, dealer_card: Card):
        if self.hand.is_soft() and 9 <= dealer_card.get_value() <= 10 and self.hand.get_value() >= 19:
            return Action.STAND
        
        if self.hand.is_soft() and self.hand.get_value() >= 18:
            return Action.STAND
        
        if not self.hand.is_soft() and 2 <= dealer_card.get_value() <= 3 and self.hand.get_value() >= 13:
            return Action.STAND
        
        if not self.hand.is_soft() and 4 <= dealer_card.get_value() <= 6 and self.hand.get_value() >= 12:
            return Action.STAND
        
        if not self.hand.is_soft() and self.hand.get_value() >= 17:
            return Action.STAND
        
        if self.hand.is_soft() and 3 <= dealer_card.get_value() <= 6 and self.hand.get_value() == 17:
            return Action.DOUBLE
        
        if self.hand.is_soft() and 4 <= dealer_card.get_value() <= 6 and self.hand.get_value() == 18:
            return Action.DOUBLE
        
        if self.hand.is_soft() and 5 <= dealer_card.get_value() <= 6 and 13 <= self.hand.get_value() <= 16:
            return Action.DOUBLE
        
        if self.hand.is_soft() and dealer_card.get_value() == 5 and self.hand.get_value() == 12:
            return Action.DOUBLE
        
        if not self.hand.is_soft() and 2 <= dealer_card.get_value() <= 6 and 9 <= self.hand.get_value() <= 11:
            return Action.DOUBLE
        
        if not self.hand.is_soft() and 2 <= dealer_card.get_value() <= 9 and 10 <= self.hand.get_value() <= 11:
            return Action.DOUBLE
        
        if not self.hand.is_soft() and 2 <= dealer_card.get_value() <= 10 and self.hand.get_value() == 11:
            return Action.DOUBLE
        
        return Action.HIT
    
class TestPlayer2(Player):
    def place_bet(self):
        self.bet = 1
        
    def run(self, dealer_card: Card):
        if self.hand.get_value() == 11 and 1 < dealer_card.get_value() < 10:
            return Action.DOUBLE
        
        if self.hand.get_value() >= 17:
            return Action.STAND
        
        return Action.HIT
        