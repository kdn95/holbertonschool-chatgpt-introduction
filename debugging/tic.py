#!/usr/bin/python3
def print_board(board):
    print("   1   2   3")
    for i in range(len(board)):
        print(i + 1, end=" ")
        for j in range(len(board[i])):
            print("|", board[i][j], end=" ")
        print("\n  -----------")

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def tic_tac_toe():
    while True:
        board = [[" "]*3 for _ in range(3)]
        player = "X"
        while not check_winner(board):
            print_board(board)
            try:
                print("Player", player + ", it's your turn.")
                row = int(input("Enter row (1, 2, or 3): "))
                col = int(input("Enter column (1, 2, or 3): "))
                if not (1 <= row <= 3) or not (1 <= col <= 3):
                    raise ValueError("Input out of range.")
                if board[row - 1][col - 1] == " ":
                    board[row - 1][col - 1] = player
                    player = "O" if player == "X" else "X"
                    if is_board_full(board) and not check_winner(board):
                        print("It's a draw!")
                        break
                else:
                    print("That spot is already taken! Try again.")
            except ValueError as e:
                print("Invalid input:", e)

        print_board(board)
        if not is_board_full(board):
            print("Player", ("O" if player == "X" else "X") + " wins!")
        else:
            print("It's a draw!")

tic_tac_toe()
