#from class_wall import *
import random

class person:

    #_walls = wall(38, 76)
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._type = 'generic'
        self._status = 'live'
        
class bomberman(person):
    #print(person.walls._board[1][1])
    def __init__(self, board):
        #point = (2, 4)
        super().__init__(2, 4)
        self._type = 'bomberman'
        self._board = board

    def create_bomberman(self):
        #walls = wall(40, 80)
        a = self._x
        b = self._y
        head = ['[','^','^',']']
        tail = [' ',']','[',' ']
        for i in range(0,4):
            self._board[a][b+i]=head[i]
        for i in range(0,4):
            self._board[a+1][b+i]=tail[i]
        #walls.display_board()       

class enemy(person):

    def __init__(self, board):
        self._type = 'enemy'        
        self._board = board        
        y = random.randint(4, 72)        
        x = random.randint(2, 36)
        while(self._check_valid(x, y)==-1):
            y = random.randint(4, 72)        
            x = random.randint(2, 36)            
        super().__init__(x, y)
        

    def _check_valid(self, x, y):
        w = self._board
        for i in range(0,2):
            for j in range(0,4):
                if(w[x+i][y+j]!=' '):
                    return -1
        return 1

    

    def create_enemy(self):
        #walls = wall(40, 80)
        a = self._x
        b = self._y
        head = [')','O','O','(']
        tail = [' ','}','{',' ']
        for i in range(0,4):
            self._board[a][b+i]=head[i]
        for i in range(0,4):
            self._board[a+1][b+i]=tail[i]
        #person._walls.display_board()
    
