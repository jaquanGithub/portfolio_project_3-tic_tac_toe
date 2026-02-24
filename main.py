import pandas as pd

tiles = [['O', 'O', 'O'],
         ['O', 'O', 'O'],
         ['O', 'O', 'O']]

board = f'''    A | B | C\n
1   {tiles[0][0]} | {tiles[0][1]} | {tiles[0][2]}
{"-"*15}
2   {tiles[1][0]} | {tiles[1][1]} | {tiles[1][2]}
{"-"*15}
3   {tiles[2][0]} | {tiles[2][1]} | {tiles[2][2]}'''

print(board)