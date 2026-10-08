from board import initial_board, move_piece, SIZE
from rules import simple_move, capture_move, promote, has_legal_moves, has_captures, has_captures_for_piece


class Checkers:
    def __init__(self):
        self.board = initial_board()
        self.player = "R"
        self.multi_piece = None

    def print_board(self):
        print("\n   " + " ".join(str(c) for c in range(SIZE)))
        for r, row in enumerate(self.board):
            print(f"{r}  " + " ".join(row))

    def run(self):
        print("Checkers — move: sr sc er ec")
        while True:
            self.print_board()
            if not self.multi_piece and not has_legal_moves(self.board, self.player):
                winner = "B" if self.player == "R" else "R"
                print(f"{winner} wins!")
                return
            raw = input(f"{self.player}> ").strip().lower().split()
            if raw == ["q"]:
                return
            if len(raw) != 4:
                print("Enter four coordinates.")
                continue
            try:
                sr, sc, er, ec = map(int, raw)
            except ValueError:
                print("Coordinates must be numbers.")
                continue
            if not all(0 <= x < SIZE for x in (sr, sc, er, ec)):
                print("Outside board.")
                continue
            if self.board[sr][sc] not in (self.player, self.player + "K"):
                print("That is not your piece.")
                continue

            start, end = (sr, sc), (er, ec)
            piece = self.board[sr][sc]
            if self.multi_piece and start != self.multi_piece:
                print("Invalid move.")
                continue

            if has_captures(self.board, self.player):
                if capture_move(self.board, self.player, start, end):
                    mid_r, mid_c = (sr + er) // 2, (sc + ec) // 2
                    captured = self.board[mid_r][mid_c]
                    self.board[mid_r][mid_c] = "."
                    move_piece(self.board, start, end)
                    promoted = promote(self.board)
                    print(f"{piece} moved from ({sr}, {sc}) to ({er}, {ec}) and captured {captured} at ({mid_r}, {mid_c}).")
                    if promoted:
                        print(f"Piece at ({er}, {ec}) was promoted to {self.board[er][ec]}!")
                    if has_captures_for_piece(self.board, self.player, end):
                        self.multi_piece = end
                        print(f"Multi-capture: Must continue capturing with {self.board[er][ec]} at ({er}, {ec}).")
                    else:
                        self.multi_piece = None
                        self.player = "B" if self.player == "R" else "R"
                else:
                    print("Invalid move.")
                    continue
            elif simple_move(self.board, self.player, start, end):
                move_piece(self.board, start, end)
                promoted = promote(self.board)
                print(f"{piece} moved from ({sr}, {sc}) to ({er}, {ec}).")
                if promoted:
                    print(f"Piece at ({er}, {ec}) was promoted to {self.board[er][ec]}!")
                self.player = "B" if self.player == "R" else "R"
            else:
                print("Invalid move.")
                continue
