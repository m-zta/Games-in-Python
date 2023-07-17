# create a 3x3 board using list comprehension
board = [[" " for _ in range(3)] for _ in range(3)]

# constants
MIN_ROW_COL = 0
MAX_ROW_COL = 2
ERROR_MESSAGE = "Invalid input. Try again."


def print_board(board):
    for i in range(len(board)):
        print(' | '.join(board[i]))
        if i < len(board) - 1:
            print("---------")
    print("\n")


def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        return False


def is_game_over(board, round_number):
    """
    Check if game is over.
    This function checks rows, columns, and diagonals for a winning combination.
    If the board is full and there is no winning combination, it is a tie.
    Return 1 if player won, 2 if tie, 0 if game is not over.
    """

    # check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return 1

    # check columns
    for col in range(len(board[0])):
        check_col = [row[col] for row in board]
        if check_col.count(check_col[0]) == len(check_col) and check_col[0] != " ":
            return 1

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 1
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 1

    # check if board is full
    if round_number == 9:
        return 2

    return 0


def switch_players(player):
    return "O" if player == "X" else "X"


def is_valid_input(row_col):
    if len(row_col) != 2:
        print("Error: Enter two values (each 0 - 2) separated by a space.")
        return False
    return True


def within_range(row_col):
    try:
        row_col = [int(i) for i in row_col]
    except ValueError:
        print(f"{ERROR_MESSAGE} Enter integers only.")
        return None

    if row_col[0] < MIN_ROW_COL or MAX_ROW_COL < row_col[0] or row_col[1] < MIN_ROW_COL or MAX_ROW_COL < row_col[1]:
        print(ERROR_MESSAGE + " Out of range.")
        return None

    return row_col


def get_row_col():
    # get move
    while True:
        try:
            # get row and col in one line
            row_col = input("Enter row and col: ").split()

            if row_col[0] == "-1":
                print("You quit the game.")
                quit()

            # check if two values are given
            if not is_valid_input(row_col):
                continue

            # convert to int
            row_col = [int(i) for i in row_col]

            # check if row and col are within range
            row_col = within_range(row_col)
            if row_col is not None:
                return row_col

        except ValueError:
            print(f"{ERROR_MESSAGE} Enter integers only.")
            continue


def main():
    player = "X"
    round_number = 0
    successful_move = True

    print("\nWelcome to TicTacToe! \nEvery turn, enter the row and column (i.e. '0 2') you want to place your move in or enter -1 to quit.")
    while True:
        if successful_move:
            print(f"\nRound {round_number}:\n")
            print_board(board)
            print(f"Player {player}'s turn.")
        else:
            print("!! That spot is taken, try again !!")

        # get row and col from user
        row, col = get_row_col()

        if make_move(board, row, col, player):
            round_number += 1
            game_over = is_game_over(board, round_number)

            if game_over == 1:
                print(f"Player {player} won!")
                break
            elif game_over == 2:
                print("It's a tie!")
                break

            player = switch_players(player)
            successful_move = True
        else:
            successful_move = False


if __name__ == "__main__":
    main()
