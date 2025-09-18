def checkmate(board_str, pawn_direction="down"):
    """
    Checks if the King 'K' is in check on a given chessboard.
    pawn_direction = "down"  -> pawns move from top to bottom
                      "up"   -> pawns move from bottom to top
    """
    try:
        rows = [row for row in board_str.strip().split('\n') if row]
        if not rows:
            print("Error: Board is empty")
            return

        board_size = len(rows)
        board = []
        king_positions = []

        for r, row_str in enumerate(rows):
            if len(row_str) != board_size:
                print("Error: Board is not square")
                return
            row_list = list(row_str)
            for c, piece in enumerate(row_list):
                if piece == 'K':
                    king_positions.append((r, c))
            board.append(row_list)

        if len(king_positions) != 1:
            print("Error: Must be exactly 1 King")
            return

        kr, kc = king_positions[0]

    except Exception as e:
        print(f"Error: {e}")
        return

    # --- 2. Rook, Bishop, Queen threats ---
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),      # rook/queen
        (-1, -1), (-1, 1), (1, -1), (1, 1)     # bishop/queen
    ]

    for dr, dc in directions:
        for i in range(1, board_size):
            r, c = kr + i * dr, kc + i * dc
            if not (0 <= r < board_size and 0 <= c < board_size):
                break
            piece = board[r][c]
            if piece != '.':
                if abs(dr) + abs(dc) == 1:  # straight
                    if piece in 'RQ':
                        print("Success")
                        return
                elif abs(dr) + abs(dc) == 2:  # diagonal
                    if piece in 'BQ':
                        print("Success")
                        return
                break  # blocked

    # --- 3. Pawn threats ---
    if pawn_direction == "down":  # pawns move down
        pawn_threats = [(kr + 1, kc - 1), (kr + 1, kc + 1)]
    else:  # pawns move up
        pawn_threats = [(kr - 1, kc - 1), (kr - 1, kc + 1)]

    for r, c in pawn_threats:
        if 0 <= r < board_size and 0 <= c < board_size:
            if board[r][c] == 'P':
                print("Success")
                return

    # --- 4. Knight threats (optional but useful) ---
    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    for dr, dc in knight_moves:
        r, c = kr + dr, kc + dc
        if 0 <= r < board_size and 0 <= c < board_size:
            if board[r][c] == 'N':
                print("Success")
                return

    # --- 5. No threats found ---
    print("Fail")
