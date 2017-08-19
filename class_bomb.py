
import random

class bomb:

    def __init__(self, pos_x, pos_y, board):
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._board = board
    
    def plant_bomb(self, time):
        a = self._pos_x
        b = self._pos_y
        head = ['[', time, time, ']']
        for i in range(0,4):
            self._board[a][b+i] = head[i]
            self._board[a+1][b+i] = head[i]

    def blast_bomb(self):
        a = self._pos_x
        b = self._pos_y
        for i in range(-4, 8):
            for j in range(0, 2):
                if(self._board[a+j][b+i] != '#'):
                    self._board[a+j][b+i] = '^'
        for i in range(-2, 4):
            for j in range(0, 4):
                if(self._board[a+i][b+j] != '#'):
                    self._board[a+i][b+j] = '^'

    def clear_bomb(self):
        a = self._pos_x
        b = self._pos_y
        for i in range(-4, 8):
            for j in range(0, 2):
                if(self._board[a+j][b+i] != '#'):
                    self._board[a+j][b+i] = ' '
        for i in range(-2, 4):
            for j in range(0, 4):
                if(self._board[a+i][b+j] != '#'):
                    self._board[a+i][b+j] = ' '
