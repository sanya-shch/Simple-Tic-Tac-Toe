# Tic Tac Toe

import random


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

winner = '-'


def display_board():
    print(
        board[0] + ' | ' + board[1] + ' | ' + board[2] + '\n' +
        board[3] + ' | ' + board[4] + ' | ' + board[5] + '\n' +
        board[6] + ' | ' + board[7] + ' | ' + board[8] + '\n'
    )


def play_game():
    display_board()

    while True:
        player_move()
        if check_if_game_over():
            break
        computer_move()
        if check_if_game_over():
            break

    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    else:
        print('Draw.')


def player_move():
    position = input_position()
    board[position] = 'X'
    display_board()


def computer_move():
    position = random_position()
    board[position] = 'O'
    display_board()


def input_position():
    while True:
        position = input('Choose a position from 1-9: ')
        position = int(position) - 1
        if position < 0 or position > 8:
            continue
        elif board[position] == '-':
            break
    return position


def random_position():
    while True:
        position = random.randint(0, 8)
        if board[position] == '-':
            break
    return position


def check_if_game_over():
    ciw = check_if_win()
    cid = check_if_draw()
    return bool(ciw + cid)


def check_if_win():
    global winner
    check_r = check_rows()
    check_c = check_columns()
    check_d = check_diagonals()

    if check_r:
        winner = check_r
        return True
    elif check_c:
        winner = check_c
        return True
    elif check_d:
        winner = check_d
        return True
    else:
        winner = '-'
    return False


def check_rows():
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def check_columns():
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return


def check_diagonals():
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return


def check_if_draw():
    if '-' not in board:
        return True
    return False


play_game()
