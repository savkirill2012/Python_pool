from collections import Counter


class Player:

    def __init__(self):
        self.opponent_turns = []
        self.score = 0

    def behavier(self):
        pass

    def add_score(self, score_to_add: int) -> None:
        self.score += score_to_add

    def get_score(self) -> int:
        return self.score

    def remember_last_turn(self, choce: bool) -> None:
        self.opponent_turns.append(choce)

    def new_gamestart(self) -> None:
        self.score = 0
        self.opponent_turns = []


class Cheater(Player):
    def __init__(self):
        super().__init__()

    def behavier(self) -> bool:
        return False


class Cooperator(Player):
    def __init__(self):
        super().__init__()

    def behavier(self) -> bool:
        return True


class Copycat(Player):
    def __init__(self):
        super().__init__()

    def behavier(self) -> bool:
        if not self.opponent_turns:
            return True
        else:
            return self.opponent_turns[-1]


class Grudger(Player):
    def __init__(self):
        super().__init__()

    def behavier(self) -> bool:
        if False in self.opponent_turns:
            return False
        else:
            return True


class Detective(Player):

    def __init__(self):
        super().__init__()
        self.turn_number = 0

    def behavier(self) -> bool:
        self.turn_number += 1

        if self.turn_number > 4:
            return self.opponent_turns[-1]  \
                if False in self.opponent_turns[:4] else False
        else:
            return False if self.turn_number == 2 else True

    def new_gamestart(self) -> None:
        super().new_gamestart()
        self.turn_number = 0


class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1: Player, player2: Player) -> None:
        player1.new_gamestart()
        player2.new_gamestart()

        self._get_game_score(player1, player2)

        if not self.registry[player1.__class__.__name__]:
            self.registry[player1.__class__.__name__] = 0
        if not self.registry[player2.__class__.__name__]:
            self.registry[player2.__class__.__name__] = 0

        self.registry[player1.__class__.__name__] += player1.get_score()
        self.registry[player2.__class__.__name__] += player2.get_score()

    def _get_game_score(self, player1: Player, player2: Player) -> None:
        for x in range(self.matches):
            first_p_res = player1.behavier()
            second_p_res = player2.behavier()
            player1.remember_last_turn(second_p_res)
            player2.remember_last_turn(first_p_res)
            if first_p_res is False and second_p_res is True:
                player1.add_score(3)
                player2.add_score(-1)
            elif first_p_res is True and second_p_res is False:
                player2.add_score(3)
                player1.add_score(-1)
            elif first_p_res is True and second_p_res is True:
                player2.add_score(2)
                player1.add_score(2)

    def top3(self):
        for i, elem in enumerate(self.registry.most_common(3)):
            print(elem[0], elem[1])


if __name__ == "__main__":
    game = Game(100)
    player1 = Cheater()
    player2 = Cooperator()
    player3 = Copycat()
    player4 = Grudger()
    player5 = Detective()

    game.play(player1, player2)
    game.play(player1, player3)
    game.play(player1, player4)
    game.play(player1, player5)
    game.play(player2, player3)
    game.play(player2, player4)
    game.play(player2, player5)
    game.play(player3, player4)
    game.play(player3, player5)
    game.play(player4, player5)

    game.top3()
