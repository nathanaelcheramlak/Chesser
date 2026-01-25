from typing import Protocol

class ChessPiece(Protocol):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.has_moved = False

    def direction(self):
        return 1 if self.color == "white" else -1

    def forward_moves(self, board):
        pass

    def capture_moves(self, board):
        pass

    def en_passant_moves(self, board):
        pass

    def available_moves(self, board):
        return (
            self.forward_moves(board)
            + self.capture_moves(board)
            + self.en_passant_moves(board)
        )

    def attack_squares(self):
        pass

    def can_promote(self):
        return self.y == 7 or self.y == 0
