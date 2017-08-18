from __future__ import print_function
import signal,copy,sys,time
import random
from class_wall import *
from class_person import *
from time_module import *
from alarm import *

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
            print("")
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    game = wall(38, 76)
    game.create_board()
    bomber = bomberman(game._board)
    bomber.create_bomberman()
    #bomber.move_up()
    #del bomber
    #bomber.create_bomberman()
    brick_count = 20
    brick = []
    for i in range(0, brick_count):
        brick.append(bricks(game._board))
        brick[i].create_bricks()
    enemy_count = 5
    killer = []
    for i in range(0, enemy_count):
        killer.append(enemy(game._board))
        killer[i].create_enemy()
    #game.display_board()
    x = 0
    while(1):
        key = input_to()
        if(key == 'a'):
            bomber.move_left()
        if(key == 'd'):
            bomber.move_right()
        if(key == 'w'):
            bomber.move_up()
        if(key == 's'):
            bomber.move_down()
        if(key == 'q'):
            print('GAME OVER')
            sys.exit(0)
        
        for i in range(0, enemy_count):
            if(x==0):
                x = random.randint(1, 4)
            #print(x)
            while(killer[i].check_move(x)==-1):
                x = random.randint(1, 4)
                #print(killer[i].check_move(x))
            if(x==1):
                killer[i].move_right()
            elif(x==2):
                killer[i].move_left()
            elif(x==3):
                killer[i].move_up()
            if(x==4):
                killer[i].move_down()

        game.display_board()

if __name__ == "__main__":
    main()       