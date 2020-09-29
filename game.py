class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.draw = 0

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def player(self, player, move):
        self.moves[player] = move

        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1

        if p1 == "Rock" and p2 == "Scissors":
            winner = 0
        elif p1 == "Scissors" and p2 == "Rock":
            winner = 1
        elif p1 == "Paper" and p2 == "Rock":
            winner = 0
        elif p1 == "Rock" and p2 == "Paper":
            winner = 1
        elif p1 == "Scissors" and p2 == "Paper":
            winner = 0
        elif p1 == "Paper" and p2 == "Scissors":
            winner = 1

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False