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
        return 0

    def display_board(self):

        for i in self._board:
            print("".join(map(str, i)))
        return 0

class bricks(wall):

    def __init__(self, board):
        super().__init__(2, 4)
        self._symbol = '%'
        self._board = board
        y = random.randint(20, 72)        
        x = random.randint(10, 36)
        while(self._check_valid(x, y)==-1):
            y = random.randint(20, 72)        
            x = random.randint(10, 36)
        self._x = x
        self._y = y     
        

    def _check_valid(self, x, y):
        w = self._board
        if(x%2!=0 or y%4!=0):
            return -1
        for i in range(0,2):
            for j in range(0,4):
                if(w[x+i][y+j]!=' '):
                    return -1
        return 1

    
    def create_bricks(self):
        #walls = wall(40, 80)
        a = self._x
        b = self._y
        for i in range(0,4):
            self._board[a][b+i]='%'
            self._board[a+1][b+i]='%'
        return 0
