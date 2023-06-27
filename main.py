from dealer import Dealer
from deck import Deck
from hand import Hand
from player import StandSoft17Player, StandPlayer, TestPlayer, TestPlayer2
from collections import defaultdict

if __name__ == '__main__':
    GAMES = 100000
    players = [StandSoft17Player(), TestPlayer(), TestPlayer2()]
    dealer = Dealer(players, StandSoft17Player(), Deck())
    # dealer.verbose = True
    for _ in range(GAMES):
        dealer.run()
        
    for player in dealer.players:
        print(f"Player {(player.__class__.__name__).rjust(17)} balance: {player.balance} results: {[(result, round(num / GAMES * 100, 2)) for result, num in player.results.items()]}")
        
    for key in sorted(players[0].win_stats):
        print(f"{key} {' '.join([str(round(player.win_stats[key] / player.game_stats[key] * 100, 2)) for player in players])}")
    # random_deck = Deck()
    # total_hands = defaultdict(int)
    # hands_bust = defaultdict(int)
    # next_values = defaultdict(list)
    
    # for _ in range(1000000):
    #     test_hand = Hand()
    #     test_hand.add_card(random_deck.get_card())
    #     test_hand.add_card(random_deck.get_card())
    #     key = ("S" if test_hand.is_soft() else "H") + str(test_hand.get_value()).zfill(2)
    #     total_hands[key] += 1
        
    #     test_hand.add_card(random_deck.get_card())
    #     has_bust = test_hand.get_value() > 21
        
    #     if has_bust:
    #         hands_bust[key] += 1
            
    #     next_values[key].append(test_hand.get_value())
            
    # for hand, count in sorted(total_hands.items()):
    #     print(f"{hand:3} {count:3d} {hands_bust[hand]:3d} {round(hands_bust[hand] / count * 100, 2):2.2f}%, {sum(next_values[hand]) / count if count > 0 else 0:2.2f}")
            
            
    
    
    