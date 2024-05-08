"""
This is a tic tac toe AI using minimax algorithm
Modules used:
  math,
  copy

Functions Made:
  minimax: the minimax algorithm,
  evaluate: evaluates the board,
  is_terminal_state: returns if the match is over,
  get_possible_moves: gives all possible moves,
  get_chance: tells whose chance it is,
  is_winner: tells if the player has won,
  main: implementation of minimax algorithm
"""

import math
import copy


def minimax(board, depth, maximizingPlayer):
    if depth == 0 or is_terminal_state(board):
        return evaluate(board)

    if maximizingPlayer:
        best_value = -math.inf
        for move in get_possible_moves(board):
            value = minimax(make_move(board, move), depth - 1, False)
            for i in board:
                print(i)
            print()
            best_value = max(best_value, value)
        return best_value

    else:
        best_value = math.inf
        for move in get_possible_moves(board):
            value = minimax(make_move(board, move), depth - 1, True)
            for i in board:
                print(i)
            print()
            best_value = min(best_value, value)
        return best_value


def evaluate(board):
    if is_winner(board, "X"):
        return 1
    elif is_winner(board, "O"):
        return -1
    else:
        return 0


def is_terminal_state(board):
    return is_winner(board, "X") or is_winner(board, "O") or len(get_possible_moves(board)) == 0


def get_possible_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                moves.append((i, j))
    return moves


def get_chance(state):
    x_count = 0
    o_count = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] == "X":
                x_count += 1
            elif state[i][j] == "O":
                o_count += 1

    if x_count > o_count:
        return "O"
    else:
        return "X"


def make_move(state, move):
    new_state = copy.deepcopy(state)
    new_state[move[0]][move[1]] = get_chance(state)
    return new_state


def is_winner(state, player):
    for i in range(3):
        if state[i][0] == player and state[i][1] == player and state[i][2] == player:
            return True

    for i in range(3):
        if state[0][i] == player and state[1][i] == player and state[2][i] == player:
            return True

    if state[0][0] == player and state[1][1] == player and state[2][2] == player:
        return True

    if state[0][2] == player and state[1][1] == player and state[2][0] == player:
        return True

    return False


def main():
    board = [
        ["-", "-", "X"],
        ["O", "X", "-"],
        ["-", "O", "X"]]
    blank = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                blank += 1
    chance = get_chance(board)
    best_move = minimax(board, blank + 1, True if chance == "X" else False)
    print(best_move)


if __name__ == "__main__":
    main()
