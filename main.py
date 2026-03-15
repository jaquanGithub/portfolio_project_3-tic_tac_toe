tiles = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
used_tiles = []

class Player:
    def __init__(self):
        self.name = ''
        self.sign = ''
        self.score = 0

def reset_board():
    global tiles, used_tiles
    tiles = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
    used_tiles = []

def update_board(tiles):
    board = f'''    A | B | C
    
1)  {tiles[0][0]} | {tiles[0][1]} | {tiles[0][2]}
   {"-"*11}
2)  {tiles[1][0]} | {tiles[1][1]} | {tiles[1][2]}
   {"-"*11}
3)  {tiles[2][0]} | {tiles[2][1]} | {tiles[2][2]}'''
    return board

def check_board(current, second):
    for column_num in range(3):
        if tiles[0][column_num] == tiles[1][column_num] == tiles[2][column_num] != " ":
            won_game(current, second)
    for row_num in range(3):
        if tiles[row_num][0] == tiles[row_num][1] == tiles[row_num][2] != " ":
            won_game(current, second)
    if tiles[0][0] == tiles[1][1] == tiles[2][2] != " ":
        won_game(current, second)
    if tiles[0][2] == tiles[1][1] == tiles[2][0] != " ":
        won_game(current, second)
    if len(used_tiles) == 9:
        tie_game(current, second)

def won_game(winner, looser):
    winner.score += 1
    print(f"\nCongrats! {winner.name} won the game!\n")
    print(f"\nCurrent score: {winner.name}/{looser.name} - {winner.score}/{looser.score}")
    print(update_board(tiles))
    another_game = input("\nWould you like to play again? (n/y)").lower()
    if another_game == 'y':
        reset_board()
        choose_player(winner, looser)
    elif another_game == 'n':
        print("Very well then. See you next time!")
        exit()
    else:
        print("Seems like you typed something wrong... No problem, the program will just stop.")
        exit()

def tie_game(current, second):
    print("\nThe game ended in a tie!\n")
    print(update_board(tiles))
    another_game = input("\nWould you like to play again? (n/y)").lower()
    if another_game == 'y':
        reset_board()
        choose_player(current, second)
    elif another_game == 'n':
        print("Very well then. See you next time!")
        exit()
    else:
        print("Seems like you typed something wrong... No problem, the program will just stop.")
        exit()

def choose_player(first_player, second_player):
    first_player.sign = input(f"{first_player.name}- Choose a symbol (x/o): ").upper()
    if first_player.sign == 'O':
        second_player.sign = 'X'
        print(f"\n{second_player.name} starts!")
        game(second_player, first_player)
    elif first_player.sign == 'X':
        second_player.sign = 'O'
        print(f"\n{first_player.name} starts!")
        game(first_player, second_player)
    else:
        print("You did not type a valid input. Try again. ")
        choose_player(first_player, second_player)

def game(current_player, other_player):
    print(f"\nIt is {current_player.name}'s turn!")
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
        game(current_player, other_player)
    row_input = input("\nChoose a row (1/2/3): ")
    if row_input == '1':
        row = 0
    elif row_input == '2':
        row = 1
    elif row_input == '3':
        row = 2
    else:
        print("Seems like you did not follow instructions... Try again.")
        game(current_player, other_player)
    if (row, column) in used_tiles:
        print("\nThat tile is taken already. Try another one.")
        game(current_player, other_player)
    else:
        used_tiles.append((row, column))
    tiles[row][column] = current_player.sign
    check_board(current_player, other_player)
    game(current_player=other_player, other_player=current_player)


player_1 = Player()
player_2 = Player()
print("Welcome to Tic Tac Toe!")
player_1.name = input("\nType name of 1st player: ").capitalize()
player_2.name = input("\nType name of 2nd player: ").capitalize()
choose_player(player_1, player_2)
