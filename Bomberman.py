from __future__ import print_function
import signal,copy,sys,time
import random
from class_wall import *
from class_person import *
from time_module import *
from alarm import *
from class_bomb import *

def main():
    getch = GetchUnix()

    def alarmHandler(signum, frame):
        raise AlarmException

    def input_to(timeout=1):
        signal.signal(signal.SIGALRM, alarmHandler)
        signal.alarm(timeout)
        try:
            text = getch()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    game = wall(38, 76)
    game.create_board()
    bomber = bomberman(game._board)
    #bomber.create_bomberman()
    #bomber.move_up()
    #del bomber
    bomber.create_bomberman()
    brick_count = 20
    brick = []
    for i in range(0, brick_count):
        brick.append(bricks(game._board))
        brick[i].create_bricks()
    enemy_count = 10
    killer = []
    for i in range(0, enemy_count):
        killer.append(enemy(game._board))
        killer[i].create_enemy()
    #game.display_board()
    x = []
    for i in range(0, enemy_count):
        x.append(0)
    blast = 0
    time = -1
    plant = 0
    lives = 3
    score = 0

    while(1):
        k = 1
        key = input_to()
        if(key == 'a'):
            for i in range(0, enemy_count):
                if(bomber.check_destroy(2, killer[i]._x, killer[i]._y) == 1):
                    bomber._die()
                    lives-=1
                    if(lives == 0):
                        print('YOUR SCORE IS: ' + str(score))
                        sys.exit(0)
                    bomber = bomberman(game._board)
                    bomber.create_bomberman()
                    k = 0
            if(k == 1):
                bomber.move_left()
        if(key == 'd'):
            for i in range(0, enemy_count):
                if(bomber.check_destroy(1, killer[i]._x, killer[i]._y) == 1):
                    bomber._die()
                    lives-=1
                    if(lives == 0):
                        print('YOUR SCORE IS: ' + str(score))
                        sys.exit(0)
                    bomber = bomberman(game._board)
                    bomber.create_bomberman()
                    k = 0
            if(k == 1):
                bomber.move_right()
        if(key == 'w'):
            for i in range(0, enemy_count):
                if(bomber.check_destroy(3, killer[i]._x, killer[i]._y) == 1):
                    bomber._die()
                    lives-=1
                    if(lives == 0):
                        print('YOUR SCORE IS: ' + str(score))
                        sys.exit(0)
                    bomber = bomberman(game._board)
                    bomber.create_bomberman()
                    k = 0
            if(k == 1):
                bomber.move_up()
        if(key == 's'):
            for i in range(0, enemy_count):
                if(bomber.check_destroy(4, killer[i]._x, killer[i]._y) == 1):
                    bomber._die()
                    lives-=1
                    if(lives == 0):
                        print('YOUR SCORE IS: ' + str(score))
                        sys.exit(0)
                    bomber = bomberman(game._board)
                    bomber.create_bomberman()
                    k = 0
            if(k == 1):
                bomber.move_down()
        if(key == 'q'):
            print('GAME QUITTED')
            sys.exit(0)
        
        if(time>=0 and plant==1):
            time-=1
            bomb1.plant_bomb(time)
            bomber.create_bomberman()
        if(blast == 1):
            bomb1.clear_bomb()
            p1 = bomb1._pos_x
            p2 = bomb1._pos_y
            if(bomber.destroy(p1, p2)==1):
                lives-=1
                if(lives == 0):
                    print('YOUR SCORE IS: ' + str(score))
                    sys.exit(0)
                bomber = bomberman(game._board)
                bomber.create_bomberman()
            for i in range(0, enemy_count):
                if(killer[i].destroy(p1, p2)==1):
                    score+=100
                    enemy_count-=1
            for i in range(0, brick_count):
                if(brick[i].destroy(p1, p2)==1):
                    score+=20
                    brick_count-=1
            blast = 0
            del bomb1
        if(key == 'x' and plant == 0):
            time = 10
            a = bomber._x
            b = bomber._y
            bomb1 = bomb(a, b, game._board)
            bomb1.plant_bomb(time)
            plant = 1
            bomber.create_bomberman()
        if(time==-1 and plant==1):
            bomb1.blast_bomb()
            blast = 1
            plant = 0
        
        for i in range(0, enemy_count):
            if(x[i]==0):
                x[i] = random.randint(1, 4)
            #print(x)
            p = killer[i].check_move1(1)
            q = killer[i].check_move1(2)
            r = killer[i].check_move1(3)
            s = killer[i].check_move1(4)
            t = killer[i].check_destroy(x[i], bomber._x, bomber._y)
            while(killer[i].check_move1(x[i])==-1 and (p == 1 or q == 1 or r == 1 or s == 1) and t == 0):
                x[i] = random.randint(1, 4)
                #print(killer[i].check_move(x))
            if(t == 1):
                bomber._die()
                lives-=1
                if(lives == 0):
                    print('YOUR SCORE IS: ' + str(score))
                    sys.exit(0)
                bomber = bomberman(game._board)
                bomber.create_bomberman()
            if(x[i]==1):
                killer[i].move_right()
            elif(x[i]==2):
                killer[i].move_left()
            elif(x[i]==3):
                killer[i].move_up()
            if(x[i]==4):
                killer[i].move_down()
        if(lives == 0):
            print('YOUR SCORE IS: ' + str(score))
            sys.exit(0)
        #bomber.create_bomberman()        
        game.display_board(score, lives, enemy_count)

if __name__ == "__main__":
    main()       