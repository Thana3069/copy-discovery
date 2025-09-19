def checkmate(board_str):
    board = [list(line) for line in board_str.splitlines() if line.strip()]
    n = len(board)

    king_pos = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    if not king_pos:
        print("Fail")
        return

    ki, kj = king_pos

    def check_pawn(i, j):
        for di, dj in [(-1, -1), (-1, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) == king_pos:
                return True
        return False

    def check_bishop(i, j):
        for di, dj in [(-1,-1), (-1,1), (1,-1), (1,1)]:
            ni, nj = i, j
            while True:
                ni += di
                nj += dj
                if not (0 <= ni < n and 0 <= nj < n):
                    break
                if (ni, nj) == king_pos:
                    return True
                if board[ni][nj] != '.':
                    break
        return False

    def check_rook(i, j):
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = i, j
            while True:
                ni += di
                nj += dj
                if not (0 <= ni < n and 0 <= nj < n):
                    break
                if (ni, nj) == king_pos:
                    return True
                if board[ni][nj] != '.':
                    break
        return False

    def check_queen(i, j):
        return check_bishop(i, j) or check_rook(i, j)

    for i in range(n):
        for j in range(n):
            piece = board[i][j]
            if piece == 'P' and check_pawn(i, j):
                print("Success")
                return
            elif piece == 'B' and check_bishop(i, j):
                print("Success")
                return
            elif piece == 'R' and check_rook(i, j):
                print("Success")
                return
            elif piece == 'Q' and check_queen(i, j):
                print("Success")
                return

    print("Fail")
