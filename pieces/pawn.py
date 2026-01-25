from utils import inbound

class Pawn:
    def __init__(self, x, y, color):
        self.name = "pawn"
        self.x = x
        self.y = y
        self.color = color
        self.has_moved = False

    def direction(self):
        return 1 if self.color == "white" else -1

    def forward_moves(self, board):
        # TODO: Pin and checks should be added
        moves = []
        if self.color == 'white':
            if board.get_piece(self.x + 1, self.y) is None:
                moves.append((self.x + 1, self.y))
            if not self.has_moved and board.get_piece(self.x + 2, self.y) is None:
                moves.append((self.x + 2, self.y))
        else:
            if board.get_piece(self.x - 1, self.y) is None:
                moves.append((self.x - 1, self.y))
            if not self.has_moved and board.get_piece(self.x - 2, self.y) is None:
                moves.append((self.x - 2, self.y))
        return moves


    def capture_moves(self, board):
        # TODO: Pin and checks should be added - WE CAN CHECK THAT AFTER APPLYING THE MOVE AND CHECK IF THE KING IS NOT IN CHECK
        moves = []
        if self.color == "white":
            if board.get_piece(self.x + 1, self.y + 1):
                moves.append((self.x + 1, self.y + 1))
            if board.get_piece(self.x - 1, self.y + 1):
                moves.append((self.x - 1, self.y + 1))
        else:
            if board.get_piece(self.x + 1, self.y - 1):
                moves.append((self.x + 1, self.y - 1))
            if board.get_piece(self.x - 1, self.y - 1):
                moves.append((self.x - 1, self.y - 1))
        return moves

    def en_passant_moves(self, board):
        last_move = board.last_move
        if last_move.piece.name != "pawn":
            return []

        if self.color == "white":
            x2, y2 = last_move.curr_coor
            
            

    def available_moves(self, board):
        return (
            self.forward_moves(board)
            + self.capture_moves(board)
            + self.en_passant_moves(board)
        )

    def attack_squares(self):
        if self.color == "white":
            return [(self.x + dx, self.y + dy) for dx, dy in [(1, 1), (1, -1)]]
        else:
            return [(self.x + dx, self.y + dy) for dx, dy in [(-1, -1), (-1, 1)]]

    def can_promote(self):
        return self.y == 7 or self.y == 0
