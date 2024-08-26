# server/game_logic.py

class Game:
    def __init__(self):
        self.board = [['' for _ in range(5)] for _ in range(5)]
        self.players = ['Player 1', 'Player 2']
        self.turn = 0

    def make_move(self, x, y, player):
        if self.board[x][y] == '':
            self.board[x][y] = player
            return True, self.check_winner()
        return False, None

    def check_winner(self):
        # Simplified win condition for example (a player who occupies the center wins)
        if self.board[2][2] != '':
            return self.board[2][2]
        return None

    def next_turn(self):
        self.turn = (self.turn + 1) % 2
        return self.players[self.turn]

    def get_board(self):
        return self.board
