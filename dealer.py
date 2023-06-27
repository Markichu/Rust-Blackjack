from hand import Hand
from card import Card
from common import Suits, Ranks, MAX_POINTS, Action, Result
from player import Player
from typing import List, Dict


class Dealer:
    def __init__(self, players, dealer, deck):
        self.players: List[Player] = players
        self.player_last_action: Dict[Player, Action] = {
            player: None for player in players
        }
        self.dealer: Player = dealer
        self.deck = deck
        self.verbose = False
        
    def clear_hands(self):
        self.dealer.hand = Hand()
        for player in self.players:
            player.hand = Hand()
            self.player_last_action[player] = None

    def run_players(self):
        for player in self.players:
            if player.hand.get_value() == MAX_POINTS:
                self.player_last_action[player] = Action.STAND
                
            if self.player_last_action[player] == Action.STAND:
                continue
                
            if self.player_last_action[player] == Action.DOUBLE:
                continue

            action = player.run(self.dealer.hand.cards[0])
            self.process_action(player, action)
        if self.verbose:
            print(self.player_last_action)
            
        is_complete = True
        for _, action in self.player_last_action.items():
            if action == Action.STAND or action == Action.DOUBLE:
                continue
            
            is_complete = False
            break
        
        return is_complete

    def run_dealer(self):
        action = self.dealer.run(self.dealer.hand)
        self.process_action(self.dealer, action)

    def process_action(self, player: Player, action: Action):
        if player is not self.dealer:
            self.player_last_action[player] = action
        
        match action:
            case Action.STAND:
                return
            case Action.HIT:
                player.hand.add_card(self.deck.get_card())
            case Action.DOUBLE:
                player.hand.add_card(self.deck.get_card())
                player.bet *= 2
            case Action.SPLIT:
                raise NotImplementedError()
            case _:
                raise NotImplementedError()
            
    def calculate_result(self):
        results = []
        for player in self.players:
            player.game_stats[player.initial_hand] += player.bet
            if player.hand.get_value() > MAX_POINTS:
                results.append(Result.LOSE)
            elif self.dealer.hand.get_value() > MAX_POINTS:
                results.append(Result.WIN)
                player.win_stats[player.initial_hand] += player.bet
            elif player.hand.get_value() > self.dealer.hand.get_value():
                results.append(Result.WIN)
                player.win_stats[player.initial_hand] += player.bet
            elif player.hand.get_value() < self.dealer.hand.get_value():
                results.append(Result.LOSE)
            else:
                results.append(Result.STANDOFF)
        return results

    def run(self):
        self.clear_hands()
        
        # draw two cards for dealer
        for _ in range(2):
            self.dealer.hand.add_card(self.deck.get_card())

        if self.verbose:
            print(f"Dealer {self.dealer.hand.cards}")

        # draw two cards for each player
        for player in self.players:
            player.place_bet()
            for _ in range(2):
                player.hand.add_card(self.deck.get_card())
                
            player.initial_hand = str(player.hand.cards[0].rank.to_char()) + ", " + str(player.hand.cards[1].rank.to_char())

            if self.verbose:
                print(f"Player {player.__class__.__name__} {player.hand.cards}")

        # run players
        while not self.run_players():
            pass

        # run dealer
        self.run_dealer()

        # calculate results
        player_results = self.calculate_result()
        
        if self.verbose:
            print(f"Dealer: {self.dealer.hand.get_value()}")
            for player in self.players:
                print(f"Player {player.__class__.__name__}: {player.hand.get_value()}")
        
        # update balance
        for player, result in zip(self.players, player_results):
            player.results[result] += 1
            match result:
                case Result.WIN:
                    player.balance += player.bet
                case Result.LOSE:
                    player.balance -= player.bet
                case Result.STANDOFF:
                    pass
                case _:
                    raise NotImplementedError()

        # print results
        if self.verbose:
            for player, result in zip(self.players, player_results):
                print(f"{player.__class__.__name__} {result}")
