#!/usr/bin/env python3.5
# -*-coding:utf-8 -*

import os

init_board = ["...","...","..."]
board = init_board

def print_board(board):
    print("+-------+-------+-------+")
    print("+       |       |       +")
    print("+  ",board[0][0],"  |  ",board[0][1],"  |  ", board[0][2],"  +")
    print("+       |       |       +")
    print("+-------+-------+-------+")
    print("+       |       |       +")
    print("+  ",board[1][0],"  |  ",board[1][1],"  |  ", board[1][2],"  +")
    print("+       |       |       +")
    print("+-------+-------+-------+")
    print("+       |       |       +")
    print("+  ",board[2][0],"  |  ",board[2][1],"  |  ", board[2][2],"  +")
    print("+       |       |       +")
    print("+-------+-------+-------+")

def check_winner(board):
    col_0 = ""
    col_1 = ""
    col_2 = ""
    nw_se = ""
    ne_sw = ""
    i = 0
    j = 2

    for row in board:
        if row == "XXX":
            return "X"
        if row == "OOO":
            return "O"
        col_0 += row[0]
        col_1 += row[1]
        col_2 += row[2]
        nw_se += row[i]
        ne_sw += row[j]
        i+=1
        j-=1

    if col_0 == "XXX" or col_1 == "XXX" or col_2 == "XXX" or nw_se == "XXX" or ne_sw == "XXX":
        return "X"
    if col_0 == "OOO" or col_1 == "OOO" or col_2 == "OOO" or nw_se == "OOO" or ne_sw == "OOO":
        return "O"
    else:
        return "D"

def game_continues(board):
    if check_winner(board) == "X" or check_winner(board) == "O":
        return False
    else:
        for row in board:
            for item in row:
                if item == ".":
                    return True
    return False

def check_input_row(row):
    if row < 0 or row > 2:
        print("ERROR: Row must be between 0 and 2")
        return False
    else:
        return True

def check_input_col(col):
    if col < 0 or col > 2:
        print("ERROR: Column must be between 0 and 2")
        return False
    else:
        return True

def check_input_coords(row,col,board):
    return board[row][col] == "."

def ask_X(board):
    print("Your turn, player X")
    do = True
    while do:
        row = int(input("Indicate row (0 - 2) : "))
        while not check_input_row(row):
            row = int(input("Indicate row (0 - 2) : "))
        col = int(input("Indicate column (0 - 2) : "))
        while not check_input_col(col):
            col = int(input("Indicate column (0 - 2) : "))
        if check_input_coords(row,col,board):
            temp = list(board[row])
            temp[col] = "X"
            board[row] = "".join(temp)
            do = False
        else:
            print("ERROR: Invalid coordinates !")

def ask_O(board):
    print("Your turn, player O")
    do = True
    while do:
        row = int(input("Indicate row (0 - 2) : "))
        while not check_input_row(row):
            row = int(input("Indicate row (0 - 2) : "))
        col = int(input("Indicate column (0 - 2) : "))
        while not check_input_col(col):
            col = int(input("Indicate column (0 - 2) : "))
        if check_input_coords(row,col,board):
            temp = list(board[row])
            temp[col] = "O"
            board[row] = "".join(temp)
            do = False
        else:
            print("ERROR: Invalid coordinates !")

i=0
while game_continues(board):
    print_board(board)
    if i%2 == 0:
        ask_X(board)
    else:
        ask_O(board)
    i+=1

print_board(board)
winner = check_winner(board)
if winner == "D":
    print("It's a DRAW !")
else:
    print("AND THE WINNER IS : PLAYER ",winner)
