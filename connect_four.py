# prints the board
def print_board(board):
    for row in board:
        for element in row:
            print(element, end=" ")
        print()

# creates the initial board
def initialize_board(num_rows, num_cols):
    board = [
        ["-" for i in range(num_cols)]
        for j in range(num_rows)
    ]
    return board

# inserts the chip at the position first checking if its empty
def insert_chip(board, col, chip_type):
    row = len(board) - 1
    initial = board[row][col]

    taken = True

    while taken:
        if initial == "-":
            board[row][col] = chip_type
            taken = False
        else:
            row -= 1
            initial = board[row][col]

# checks the winner horizontally then vertically
def check_if_winner(board, col, row, chip_type):
    # Check horizontal
    for i in range(row):
        count = 0
        for j in range(col):
            if board[i][j] == chip_type:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # Check vertical
    for k in range(col):
        count = 0
        for m in range(row):
            if board[m][k] == chip_type:
                count += 1
                if count == 4:
                    return True

    return False

# main function
def main():
    a = int(input("What would you like the height of the board to be? "))
    b = int(input("What would you like the length of the board to be? "))

    board = initialize_board(a, b)
    print_board(board)
    print()
    print("Player 1: x")
    print("Player 2: o")
    print()

    player = 1
    chip = "x"

    count1 = 0

    while True:
        col = int(input(f"Player {player}: Which column would you like to choose? "))
        insert_chip(board, col, chip)
        count1 += 1
        print_board(board)
        print()
        if check_if_winner(board, b, a, chip):
            print(f"Player {player} won the game!")
            break

        if count1 == a * b:
            print("Draw. Nobody wins.")
            break

        if player == 1:
            player = 2
        else:
            player = 1

        if chip == "x":
            chip = "o"
        else:
            chip = "x"


if __name__ == '__main__':
    main()
