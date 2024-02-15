#!/usr/bin/python3

def initialize_board():
    """Initializes the game board."""
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    """Prints the game board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board):
    """Checks if there is a win in the game."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def check_tie(board):
    """Checks if the game is a tie."""
    for row in board:
        if " " in row:
            return False
    return True

def player_move(board, player):
    """Allows a player to make a move."""
    while True:
        try:
            row = int(input(f"Player {player}, enter your row (0-2): "))
            col = int(input(f"Player {player}, enter your column (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter numbers only.")

def tic_tac_toe():
    """Runs the Tic Tac Toe game."""
    board = initialize_board()
    current_player = "X"

    while True:
        print_board(board)
        player_move(board, current_player)

        if check_win(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
