class Move:
    def __init__(self, piece, color, is_capture=False, is_check=False, x1, y1, x2, y2):
        self.piece = piece
        self.color = color
        self.prev_coor = (x1, y1)
        self.curr_coor = (x2, y2)

        self.is_capture = is_capture
        self.is_check = is_check