def checkmate(boardInput):
    lines = boardInput.strip().split('\n')
    board = []
    for row in lines: 
        board.append(list(row.lstrip())) 
    size = len(board)


    kingPosition = None
    kingCount = 0

    for y in range(size):
        for x in range(len(board[y])):
            if board[y][x] == 'K':
                kingPosition = (y, x)
                kingCount += 1

    if not kingPosition:
        print("Error: No king in the board")
        return
    elif kingCount > 1:
        print("Error: More than 1 king in the board")
        return


    def inBounds(y, x): 
        if y < 0 or y >= size:
            return False
        if x < 0 or x >= len(board[y]):
            return False
        return True


    def pawn():
        for dy, dx in [(1, -1), (1, 1)]:
            ny = kingPosition[0] + dy
            nx = kingPosition[1] + dx
            if inBounds(ny, nx) and board[ny][nx] == 'P':
                return True
        return False


    def bishop():
        for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            ny = kingPosition[0]
            nx = kingPosition[1]
            while True:
                ny += dy
                nx += dx
                if not inBounds(ny, nx):
                    break
                if board[ny][nx] != '.':
                    if board[ny][nx] == 'B':
                        return True
                    break
        return False


    def rook():
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny = kingPosition[0]
            nx = kingPosition[1]
            while True:
                ny += dy
                nx += dx
                if not inBounds(ny, nx):
                    break
                if board[ny][nx] != '.':
                    if board[ny][nx] == 'R':
                        return True
                    break
        return False


    def queen():
        for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1),
                       (-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny = kingPosition[0]
            nx = kingPosition[1]
            while True:
                ny += dy
                nx += dx
                if not inBounds(ny, nx):
                    break
                if board[ny][nx] != '.':
                    if board[ny][nx] == 'Q':
                        return True
                    break
        return False


    if pawn() or bishop() or rook() or queen():
        print("Success")
    else:
        print("Fail")