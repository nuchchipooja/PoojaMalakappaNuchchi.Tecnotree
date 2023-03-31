#TIC-TAC-TOE

def print_board(board):
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("-+-+-")
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("-+-+-")
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])

def check_winner(board):
    # check rows
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[0] != "-":
            return row[0]
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != "-":
            return board[0][i]
    # check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]
    # no winner
    return None

def tic_tac_toe():
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    current_player = "X"
    winner = None
    while winner is None:
        print_board(board)
        row = int(input("Enter row number (0-2): "))
        col = int(input("Enter column number (0-2): "))
        if board[row][col] == "-":
            board[row][col] = current_player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
            winner = check_winner(board)
    print_board(board)
    print(winner + " wins!")

tic_tac_toe()
