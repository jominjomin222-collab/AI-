
# Tic Tac Toe Game

board = [' ' for _ in range(9)]

def display_board():
    print()
    for i in range(3):
        print(" | ".join(board[i*3:i*3+3]))
        if i < 2:
            print("---------")
    print()

def check_winner(player):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for position in winning_positions:
        if all(board[i] == player for i in position):
            return True
    return False

def tic_tac_toe():
    player = 'X'

    print("Welcome to Tic Tac Toe!")
    print("Enter positions from 1 to 9")

    while True:
        display_board()

        try:
            move = int(input("Player " + player + ", enter position: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if move < 1 or move > 9 or board[move - 1] != ' ':
            print("Invalid move! Try again.")
            continue

        board[move - 1] = player

        if check_winner(player):
            display_board()
            print("Player", player, "wins!")
            break

        if ' ' not in board:
            display_board()
            print("Match Draw!")
            break

        player = 'O' if player == 'X' else 'X'

tic_tac_toe()
