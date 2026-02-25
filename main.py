import pandas as pd

tiles = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

board = f'''    A | B | C\n
1   {tiles[0][0]} | {tiles[0][1]} | {tiles[0][2]}
{"-"*15}
2   {tiles[1][0]} | {tiles[1][1]} | {tiles[1][2]}
{"-"*15}
3   {tiles[2][0]} | {tiles[2][1]} | {tiles[2][2]}'''

def update_board(tiles):
    board = f'''    A | B | C\n
1   {tiles[0][0]} | {tiles[0][1]} | {tiles[0][2]}
{"-"*15}
2   {tiles[1][0]} | {tiles[1][1]} | {tiles[1][2]}
{"-"*15}
3   {tiles[2][0]} | {tiles[2][1]} | {tiles[2][2]}'''
    return board

def choose_player():
    player_1 = input("Player 1- Choose a symbol (x/o): ").upper()
    if player_1 == 'O':
        player_2 = 'X'
        print("\nPlayer 2 starts!")
        game(player_2)
    elif player_1 == 'X':
        print("\nPlayer 1 starts!")
        game(player_1)
    else:
        print("You did not type a valid input. Try again. ")
        choose_player()

def game(player):
    print(f"\nIt is {player}'s turn!")
    print(update_board(tiles))
    column_input = input("\nChoose a column (a/b/c): ").lower()
    if column_input == 'a':
        column = 0
    elif column_input == 'b':
        column = 1
    elif column_input == 'c':
        column = 2
    else:
        print("\nSeems like you did not follow instructions... Try again.")
        game(player)
    row_input = input("\nChoose a row (1/2/3): ")
    if row_input == '1':
        row = 0
    elif row_input == '2':
        row = 1
    elif row_input == '3':
        row = 2
    else:
        print("Seems like you did not follow instructions... Try again.")
        game(player)
    tiles[row][column] = player
    game(swap_player(player))

def swap_player(player):
    if player == 'X':
        current_player = "O"
    else:
        current_player = "X"
    return current_player

print("Welcome to Tic Tac Toe!\n")
choose_player()