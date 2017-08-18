from class_person import *
import random

class wall:
    
    def __init__(self, length, breadth):
        self._length = length
        self._breadth = breadth
        self._symbol = '#'
        self._board = [[' ' for x in range(breadth)] for y in range(length)]

    def create_board(self):

        b = self._breadth
        a = self._length
        for i in range(0, b):
            self._board[0][i]=self._board[a-1][i]='#'
            self._board[1][i]=self._board[a-2][i]='#'
    
        for i in range(0,a):
            self._board[i][0]=self._board[i][b-1]='#'
            self._board[i][1]=self._board[i][b-2]='#'
            self._board[i][2]=self._board[i][b-3]='#'
            self._board[i][3]=self._board[i][b-4]='#'
        
        i=4
        while(i<36):
            j=8
            while(j<76):
                for k in range(0,4):
                    self._board[i][j+k]='#'
                    self._board[i+1][j+k]='#'
                j+=8
            i+=4 

    def display_board(self):

        for i in self._board:
            print("".join(map(str, i)))

class bricks(wall):


def main():
    game = wall(38, 76)
    game.create_board()
    bomber = bomberman(game._board)
    bomber.create_bomberman()
    enemy_count = 5
    for i in range(0, enemy_count):
        killer = enemy(game._board)
        killer.create_enemy()
    game.display_board()

if __name__ == "__main__":
    main()        

