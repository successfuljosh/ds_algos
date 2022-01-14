class Leaderboard:

    def __init__(self):
        self.board = dict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.board:
            self.board[playerId] += score
            return
        self.board[playerId] = score

    def top(self, K: int) -> int:
        sorted_dic = dict(sorted(self.board.items(), key=lambda item: item[1], reverse=True))
        return sum(list(sorted_dic.values())[0:K])

    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0
