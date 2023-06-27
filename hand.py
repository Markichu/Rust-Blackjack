from common import Ranks
from card import Card
from typing import List

class Hand:
    def __init__(self):
        self.cards: List[Card] = []
        
    def add_card(self, card):
        self.cards.append(card)
        
    def only_first_card(self):
        first_card = Hand()
        first_card.add_card(self.cards[0])
        return first_card
    
    def is_soft(self):
        raw_total = sum([card.get_value() for card in self.cards])
        ace_count = sum([card.rank == Ranks.ACE for card in self.cards])
        return ace_count > 0 and raw_total <= 11
        
    def get_value(self):
        total = sum([card.get_value() for card in self.cards])
        
        ace_count = sum([card.rank == Ranks.ACE for card in self.cards])
        if total <= 11 and ace_count > 0:
            total += 10
            
        return total
    
    def __repr__(self):
        return f"<{', '.join(str(card) for card in self.cards)}>"