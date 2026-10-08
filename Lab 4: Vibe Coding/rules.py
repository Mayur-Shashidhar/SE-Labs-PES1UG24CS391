SIZE = 8


def simple_move(board, player, start, end):
    sr, sc = start
    er, ec = end
    piece = board[sr][sc]
    is_king = piece.endswith("K")
    direction = -1 if player == "R" else 1
    return (
        board[er][ec] == "." and
        abs(er - sr) == 1 and abs(ec - sc) == 1 and
        (is_king or er - sr == direction)
    )


def capture_move(board, player, start, end):
    sr, sc = start
    er, ec = end
    piece = board[sr][sc]
    is_king = piece.endswith("K")
    direction = -1 if player == "R" else 1
    mr, mc = (sr + er) // 2, (sc + ec) // 2
    opponent = "B" if player == "R" else "R"
    return (
        board[er][ec] == "." and
        abs(er - sr) == 2 and abs(ec - sc) == 2 and
        (is_king or er - sr == 2 * direction) and
        board[mr][mc] in (opponent, opponent + "K")
    )


def promote(board):
    promoted = False
    for c in range(SIZE):
        if board[0][c] == "R":
            board[0][c] = "RK"
            promoted = True
        if board[SIZE - 1][c] == "B":
            board[SIZE - 1][c] = "BK"
            promoted = True
    return promoted


def has_captures_for_piece(board, player, start):
    r, c = start
    for dr, dc in ((-2, -2), (-2, 2), (2, -2), (2, 2)):
        end = (r + dr, c + dc)
        if 0 <= end[0] < SIZE and 0 <= end[1] < SIZE:
            if capture_move(board, player, start, end):
                return True
    return False


def has_captures(board, player):
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] in (player, player + "K"):
                if has_captures_for_piece(board, player, (r, c)):
                    return True
    return False


def has_legal_moves(board, player):
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] in (player, player + "K"):
                start = (r, c)
                if has_captures_for_piece(board, player, start):
                    return True
                for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    end = (r + dr, c + dc)
                    if 0 <= end[0] < SIZE and 0 <= end[1] < SIZE:
                        if simple_move(board, player, start, end):
                            return True
    return False
