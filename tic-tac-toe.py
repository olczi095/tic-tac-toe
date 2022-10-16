# ---------------
# WORK TO DO:
#
# 1. Function with active game
# 2. Create empty board
# 3. Drawing board (checking if it's empty or not)
# 4. Change player
# 5. Result of the game:
#     a) tie
#     b) win:
#         - diagonals
#         - horizontal lines
#         - vertical lines


def the_game():
    """The 'tic-tac-toe' game for two players.
    Both players move successively until one of them wins or the game ends with a tie."""

    board = [['_' for x in range(3)] for x in range(3)]

    def printing_board():
        return board


    def diagonal_win(fill_board):
        #Check if someone won on the diagonal lines.
        return fill_board[1][1] == fill_board[0][0] ==  fill_board[2][2] or fill_board[0][2] == fill_board[1][1] == fill_board[2][0]


    def horizontal_win(fill_board):
        #Check if someone won on the horizontal lines.
        for x in range(3):
            if len(set(fill_board[x])) == 1:
                return fill_board[x][0]
        return False


    def vertical_win(fill_board):
        #Check if someone won on the diagonals.
        for x in range(3):
            if fill_board[0][x] == fill_board[1][x] == fill_board[2][x]:
                return True
        return False


    def check_the_winner(fill_board):
        if not horizontal_win(fill_board):
            if

        elif diagonal_win(fill_board):

        elif vertical_win(fill_board):


    print("\nHello players!\nThis is a tic-tac-toe game. Let's start!\n" + "-" * 30 + "\n\n")

    # player1 = input("Player 1 type your name:\n>>> ")
    hello <p1> you will have an sign.
    # player2 = input("Player 2 type your name:\n>>> ")
    print("\n\n")




the_game()