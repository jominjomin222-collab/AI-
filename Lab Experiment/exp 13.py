
# Minimax Algorithm for Tic Tac Toe

board = [' ' for _ in range(9)]

def display_board():
    for i in range(3):
        print(" | ".join(board[i*3:i*3+3]))
        if i < 2:
            print("---------")

def check_winner(b, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    return any(all(b[i] == player for i in pos)
               for pos in win_positions)

def minimax(b, is_maximizing):
    if check_winner(b, 'O'):
        return 1

    if check_winner(b, 'X'):
        return -1

    if ' ' not in b:
        return 0

    if is_maximizing:
        best_score = -float('inf')

        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, False)
                b[i] = ' '
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = float('inf')

        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, True)
                b[i] = ' '
                best_score = min(score, best_score)

        return best_score

def best_move():
    best_score = -float('inf')
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    return move

def play_game():
    print("Tic Tac Toe using Minimax Algorithm")
    print("You are X and Computer is O")
    print("Enter positions from 1 to 9")

    while True:
        display_board()

        try:
            move = int(input("Enter your move: ")) - 1
        except ValueError:
            print("Enter a valid number.")
            continue

        if move < 0 or move >= 9 or board[move] != ' ':
            print("Invalid move! Try again.")
            continue

        board[move] = 'X'

        if check_winner(board, 'X'):
            display_board()
            print("You win!")
            break

        if ' ' not in board:
            display_board()
            print("Match Draw!")
            break

        computer_move = best_move()
        board[computer_move] = 'O'

        print("Computer chooses position:", computer_move + 1)

        if check_winner(board, 'O'):
            display_board()
            print("Computer wins!")
            break

        if ' ' not in board:
            display_board()
            print("Match Draw!")
            break

play_game()
