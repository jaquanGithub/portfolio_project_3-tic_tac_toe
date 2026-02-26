tiles = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
used_tiles = []
def reset_board():
    global tiles, used_tiles
    tiles = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
    used_tiles = []

def update_board(tiles):
    board = f'''    A | B | C\n
1   {tiles[0][0]} | {tiles[0][1]} | {tiles[0][2]}
{"-"*15}
2   {tiles[1][0]} | {tiles[1][1]} | {tiles[1][2]}
{"-"*15}
3   {tiles[2][0]} | {tiles[2][1]} | {tiles[2][2]}'''
    return board

def check_board():
    for column_num in range(3):
        if tiles[0][column_num] == tiles[1][column_num] == tiles[2][column_num] != " ":
            won_game(tiles[0][column_num])
    for row_num in range(3):
        if tiles[row_num][0] == tiles[row_num][1] == tiles[row_num][2] != " ":
            won_game(tiles[row_num][0])
    if tiles[0][0] == tiles[1][1] == tiles[2][2] != " ":
        won_game(tiles[0][0])
    if tiles[0][2] == tiles[1][1] == tiles[2][0] != " ":
        won_game(tiles[0][2])
    if len(used_tiles) == 9:
        tie_game()

def won_game(who):
    print(f"\nCongrats! {who} won the game!\n")
    print(update_board(tiles))
    another_game = input("\nWould you like to play again? (n/y)").lower()
    if another_game == 'y':
        reset_board()
        choose_player()
    elif another_game == 'n':
        print("Very well then. See you next time!")
        exit()
    else:
        print("Seems like you typed something wrong... No problem, the program will just stop.")
        exit()

def tie_game():
    print("\nThe game ended in a tie!\n")
    print(update_board(tiles))
    another_game = input("\nWould you like to play again? (n/y)").lower()
    if another_game == 'y':
        reset_board()
        choose_player()
    elif another_game == 'n':
        print("Very well then. See you next time!")
        exit()
    else:
        print("Seems like you typed something wrong... No problem, the program will just stop.")
        exit()

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

def swap_player(player):
    if player == 'X':
        current_player = "O"
    else:
        current_player = "X"
    return current_player

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
    if (row, column) in used_tiles:
        print("\nThat tile is taken already. Try another one.")
        game(player)
    else:
        used_tiles.append((row, column))
    tiles[row][column] = player
    check_board()
    game(swap_player(player))

print("Welcome to Tic Tac Toe!\n")
choose_player()

# TODO - Add game functionality, Seeing if someone won.