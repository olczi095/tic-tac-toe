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


    def diagonal_win(game_board):
        #Check if someone won on the diagonal lines.
        if game_board[1][1] == game_board[0][0] ==  game_board[2][2] or game_board[0][2] == game_board[1][1] == game_board[2][0]:
            if game_board[1][1] != '_':
                return game_board[1][1]
        return False


    def horizontal_win(game_board):
        #Check if someone won on the horizontal lines.
        for x in range(3):
            if len(set(game_board[x])) == 1:
                if game_board[x][0] != '_':
                    return game_board[x][0]
        return False


    def vertical_win(game_board):
        #Check if someone won on the diagonals.
        for x in range(3):
            if game_board[0][x] == game_board[1][x] == game_board[2][x]:
                if game_board[0][x] != '_':
                    return game_board[0][x]
        return False


    def if_someone_win(game_board):
        #Check if someone already won or not.
        if horizontal_win(game_board):
            return horizontal_win(game_board)

        elif diagonal_win(game_board):
            return diagonal_win(game_board)

        elif vertical_win(game_board):
            return vertical_win(game_board)


    def game(board, player, position):
        position = position - 1
        row = position // 3
        column = position % 3
        if board[row][column] == '_':
            if player == player1:
                board[row][column] = 'X'
            else:
                board[row][column] = 'O'
        else:
            return False


    print("\nHello players!\nThis is a tic-tac-toe game. Let's start!\n" + "-" * 30 + "\n\n")

    player1 = input("Player 1 type your name:\n>>> ")
    player2 = input("Player 2 type your name:\n>>> ")
    print(f"\nHello players! {player1} has a sign 'X' and {player2} has a sign 'O'. You can choose the location from 1 to 9. "
          f"{player1} you start!\n")
    print(board)
    print("\n")

    game_continue = True

    while game_continue:
        move_p1 = int(input(f"{player1} type your number: "))
        if game(board, player1, move_p1) is False:
            break
        else:
            print(board)
            if not if_someone_win(board):
                move_p2 = int(input(f"{player2} type your number: "))
                if game(board, player2, move_p2) is False:
                    break
                else:
                    print(board)


the_game()