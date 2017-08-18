import random

def main():
    a = 40
    b = 80
    board = [[' ' for x in range(b)] for y in range(a)]

    for i in range(0,b):
        board[0][i]=board[a-1][i]='#'
        board[1][i]=board[a-2][i]='#'
    
    for i in range(0,a):
        board[i][0]=board[i][b-1]='# '
        board[i][1]=board[i][b-2]='#'
        board[i][2]=board[i][b-3]='#'
        board[i][3]=board[i][b-4]='#'

    for i in board:
        print("".join(map(str, i)))
        
if __name__ == "__main__":
    main()