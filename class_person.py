#from class_wall import *
import random

class person:

    #_walls = wall(38, 76)
    def __init__(self, x, y, board):
        self._x = x
        self._y = y
        self._type = 'generic'
        self._status = 'live'
    

    def move_right(self):
        if(self.check_move(1)==1):
            x = self._x
            y = self._y
            for i in range(0,4):
                self._board[x][y+4-i]=self._board[x][y+3-i]
                self._board[x+1][y+4-i]=self._board[x+1][y+3-i]
            self._board[x][y]=' '
            self._board[x+1][y]=' '
            self._y+=1

    def move_left(self):
        if(self.check_move(2)==1):
            x = self._x
            y = self._y
            for i in range(0,4):
                self._board[x][y+i-1]=self._board[x][y+i]
                self._board[x+1][y+i-1]=self._board[x+1][y+i]
            self._board[x][y+3]=' '
            self._board[x+1][y+3]=' '
            self._y-=1

    def move_up(self):
        if(self.check_move(3)==1):
            x = self._x
            y = self._y
            for i in range(0,3):
                for j in range(0 ,4):
                    if(i==2):
                        self._board[x+i-1][y+j] = ' '
                    else:
                        self._board[x+i-1][y+j]=self._board[x+i][y+j]
            self._x-=1
        

    def move_down(self):
        if(self.check_move(4)==1):
            x = self._x
            y = self._y
            for i in range(0,3):
                for j in range (0 ,4):
                    if(i==2):
                        self._board[x+2-i][y+j] = ' '
                    else:
                        self._board[x+2-i][y+j]=self._board[x+1-i][y+j]
            self._x+=1

    def check_move(self, key):
        w = self._board
        a = self._x
        b = self._y
        if(key == 1): 
            for i in range(0, 2):
                if(w[a+i][b+4]!=' '):
                    return -1
            return 1
        elif(key == 2):
            for i in range(0, 2):
                if(w[a+i][b-1]!=' '):
                    return -1
            return 1
        elif(key == 3):
            for i in range(0, 4):
                if(w[a-1][b+i]!=' '):
                    return -1
            return 1
        elif(key == 4):
            for i in range(0, 4):
                if(w[a+2][b+i]!=' '):
                    return -1
            return 1

    def check_move1(self, key):
        w = self._board
        a = self._x
        b = self._y
        if(key == 1): 
            for i in range(0, 2):
                if(w[a+i][b+4]!=' '):
                    return -1
            return 1
        elif(key == 2):
            for i in range(0, 2):
                if(w[a+i][b-1]!=' '):
                    return -1
            if(b-1<12 and a<6):
                return -1
            return 1
        elif(key == 3):
            for i in range(0, 4):
                if(w[a-1][b+i]!=' '):
                    return -1
                if(a-1<6 and b<12):
                    return -1
            return 1
        elif(key == 4):
            for i in range(0, 4):
                if(w[a+2][b+i]!=' '):
                    return -1
            return 1

    def check_destroy(self, key, x, y):
        w = self._board
        a = self._x
        b = self._y
        if(key == 1):
            if((b+4 == y) and (x<=a<=x+1 or x<=a+1<=x+1)):
                return 1
            return 0
        if(key == 2):
            if((b-1 == y+3) and (x<=a<=x+1 or x<=a+1<=x+1)):
                return 1
            return 0
        if(key == 3):
            if((a-1 == x+1) and (y<=b<=y+3 or y<=b+3<=y+3)):
                return 1
            return 0
        if(key == 4):
            if((a+2 == x) and (y<=b<=y+3 or y<=b+3<=y+3)):
                return 1
            return 0



    def _die(self):
        a = self._x
        b = self._y
        for i in range(0, 2):
            for j in range(0, 4):
                self._board[a+i][b+j] = ' '
        del self

    def destroy(self, a, b):
        p1 = self._x
        p2 = self._y
        if((b-4<=p2<=b+7 or b-4<=p2+3<=b+7) and (a<=p1<=a+1 or a<=p1+1<=a+1)):
            #self._die()
            return 1
        if((a-2<=p1<=a+3 or a-2<=p1+1<=a+4) and (b<=p2<=b+3 or b<=p2+3<=b+3)):
            #self._die()
            return 1
        return 0

class bomberman(person):
    #print(person.walls._board[1][1])
    def __init__(self, board):
        #point = (2, 4)
        super().__init__(2, 4, board)
        self._type = 'bomberman'
        self._board = board

    def create_bomberman(self):
        #walls = wall(40, 80)
        a = self._x
        b = self._y
        head = ['[','^','^',']']
        tail = ['.',']','[','.']
        for i in range(0,4):
            self._board[a][b+i]=head[i]
        for i in range(0,4):
            self._board[a+1][b+i]=tail[i]
        #walls.display_board()       

class enemy(person):

    def __init__(self, board):
        self._type = 'enemy'        
        self._board = board        
        y = random.randint(12, 70)        
        x = random.randint(6, 30)
        while(self._check_valid(x, y)==-1):
            y = random.randint(20, 72)        
            x = random.randint(10, 36)            
        super().__init__(x, y, board)
        

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
        tail = ['.','}','{','.']
        for i in range(0,4):
            self._board[a][b+i]=head[i]
            self._board[a+1][b+i]=tail[i]
        #person._walls.display_board()
    
