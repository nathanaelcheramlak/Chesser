class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_board()

        self.turn = "white"
        self.move_count = 0
        self.white_king_coordinate = (4, 0)
        self.black_king_coordinate = (4, 7)

        # Useful for castling
        self.white_king_moved = False
        self.black_king_moved = False
        self.white_rook_moved = [False, False]
        self.black_rook_moved = [False, False]

        # Useful for enpassant
        self.last_move = None # object of Move
        
        self.is_check = False
        self.is_checkmate = False
        self.is_stalemate = False
    
    def initialize_board(self):
        # initialize pieces
        for row in range(8):
            for col in range(8):
                # Empty cells
                if row > 1 and row < 6: # Empty cells
                    continue
                elif row == 1: # White Pawns
                    self.board[row][col] = Pawn(col, row, "white")
                elif row == 6: # Black Pawns
                    self.board[row][col] = Pawn(col, row, "black")
                elif row == 0: # White Pieces
                    if col == 0 or col == 7:
                        self.board[row][col] = Rook(col, row, "white")
                    if col == 1 or col == 6:
                        self.board[row][col] = Knight(col, row, "white")
                    if col == 2 or col == 5:
                        self.board[row][col] = Bishop(col, row, "white")
                    if col == 3:
                        self.board[row][col] = Queen(col, row, "white")
                    if col == 4:
                        self.board[row][col] = King(col, row, "white")         
                else: # Black Pieces
                    if col == 0 or col == 7:
                        self.board[row][col] = Rook(col, row, "black")
                    if col == 1 or col == 6:
                        self.board[row][col] = Knight(col, row, "black")
                    if col == 2 or col == 5:
                        self.board[row][col] = Bishop(col, row, "black")
                    if col == 3:
                        self.board[row][col] = Queen(col, row, "black")
                    if col == 4:
                        self.board[row][col] = King(col, row, "black")         
                                   
    
    def get_piece(self, x, y):
        return self.board[x][y]
    
    def set_piece(self, x, y, piece):
        self.board[x][y] = piece
    
    def change_turn(self):
        self.turn = "black" if self.turn == "white" else "white"
    
    def remove_piece(self, x, y):
        self.board[x][y] = None
    
    def move_piece(self, x1, y1, x2, y2):
        piece = self.get_piece(x1, y1)
        if piece.name == "king":
            TODO
            pass
        self.set_piece(x2, y2)
        self.remove_piece(x1, y1)
        # Check if the square it is in attacks the king
        self.change_turn()
    
    def capture(self, capturer, captured):
        self.remove_piece(captured.x, captured.y)
        self.set_piece(capturer.x, capturer.y, capturer)
        self.change_turn()
    
    def check_check(self):
        if self.turn == "white": # Check if white's king is in check cause black just moved
            for row in range(8):
                for col in range(8):
                    piece = get_piece(row, col)
                    if not piece or piece.color == "white":
                        continue
                    
                    squares_attacked = piece.available_moves(self.board)

                    

        