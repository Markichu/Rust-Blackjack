from common import Suits, Ranks
from card import Card
import random

class Deck:
    def get_card(self):
        random_suit = random.choice(list(Suits))
        random_rank = random.choice(list(Ranks))
        
        return Card(random_suit, random_rank)