# ---------------
# WORK TO DO:
#
# 1. Create nice board to display to the user.
# 2. Create a loop for users could decide if the want to play once again.
# 3. Try to clean the code.


def the_game():
    """The 'tic-tac-toe' game for two players.
    Both players move successively until one of them wins or the game ends with a tie."""

    board = [['_' for _ in range(3)] for _ in range(3)]

    def diagonal_win(game_board):
        # Check if someone won on the diagonal lines.
        if game_board[1][1] == game_board[0][0] == game_board[2][2] or game_board[0][2] == game_board[1][1] == \
                game_board[2][0]:
            if game_board[1][1] != '_':
                return game_board[1][1]
        return False

    def horizontal_win(game_board):
        # Check if someone won on the horizontal lines.
        for x in range(3):
            if len(set(game_board[x])) == 1:
                if game_board[x][0] != '_':
                    return game_board[x][0]
        return False

    def vertical_win(game_board):
        # Check if someone won on the diagonals.
        for x in range(3):
            if game_board[0][x] == game_board[1][x] == game_board[2][x]:
                if game_board[0][x] != '_':
                    return game_board[0][x]
        return False

    def if_someone_win(game_board):
        # Check if someone already won or not.
        if horizontal_win(game_board):
            return horizontal_win(game_board)

        elif diagonal_win(game_board):
            return diagonal_win(game_board)

        elif vertical_win(game_board):
            return vertical_win(game_board)

    def play_again(user_answer):
        # If users want to play again
        if user_answer.upper() == 'YES':
            the_game()

    def game(g_board, player, position):
        # Function with the right game.
        if position in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # Check if the user input is correct (number from 1 to 9)
            position = int(position)
            position = position - 1
            row = position // 3
            column = position % 3

            if g_board[row][column] == '_':
                if player == player1:
                    g_board[row][column] = 'X'
                else:
                    g_board[row][column] = 'O'

        else:
            return False

    print("\nHello players!\nThis is a tic-tac-toe game. Let's start!\n" + "-" * 30 + "\n\n")

    player1 = input("Player 1 type your name:\n>>> ")
    player2 = input("Player 2 type your name:\n>>> ")

    print(
        f"\nHello players! {player1} has a sign 'X' and {player2} has a sign 'O'. "
        f"You can choose the location from 1 to 9. "
        f"{player1} you start!\n")

    print(board)
    print("\n")

    game_continue = True

    while game_continue:

        if if_someone_win(board):
            print(f"{player2} won!!!")
            break

        else:

            move_p1 = input(f"{player1} type your number: ")

            while game(board, player1, move_p1) is False:
                # Check if the place chosen by the player1 is already filled or the input is wrong.
                print("Your choice is wrong. Try again! ")
                print(f"{board}\n")
                move_p1 = input(f"{player1} type your number: ")

            else:

                print(f"{board}\n")
                if not if_someone_win(board):
                    move_p2 = input(f"{player2} type your number: ")

                    while game(board, player2, move_p2) is False:
                        # Check if the place chosen by the player2 is already filled or the input is wrong.
                        print("Your choice is wrong. Try again! ")
                        print(f"{board}\n")
                        move_p2 = input(f"{player2} type your number: ")

                    else:

                        print(f"{board}\n")
                else:

                    print(f"{player1} won!!!")
                    game_continue = False

    play_again(input(f"\nDo you want to play again? Type 'yes' or 'no'.\n>>> "))


the_game()
