board=[]
rand=0
stop=0
def player_input():
    print('WELCOME TO TIC TAC TOE...')
    p1,p2=player_marker()
    global stop
    global board
    global rand
    board = ['', '', '', '', '', '', '', '', '', '']
    while stop!=1:
        if ((board[1]=='X'or board[1]=='O') and (board[2]=='X'or board[2]=='O') and (board[3]=='X'or board[3]=='O') and (board[4]=='X'or board[4]=='O') and (board[5]=='X'or board[6]=='O') and (board[7]=='X'or board[7]=='O') and (board[8]=='X'or board[8]=='O') and (board[9]=='X' or board[9]=='O')) :
            print('Match Tie')
            stop=1
        if rand==1:
            pos1=int(input('Player 1 Enter the position:'))
            board[pos1]=p1
            disp_board(board)
            stop=win_check()
            pos2=int(input('Player 2 Enter the position:'))
            board[pos2]=p2
            disp_board(board)
            stop=win_check()
        else:
            pos1 = int(input('Player 2 Enter the position:'))
            board[pos1] = p1
            disp_board(board)
            stop=win_check()
            pos2 = int(input('Player 1 Enter the position:'))
            board[pos2] = p2
            disp_board(board)
            stop=win_check()
def disp_board(board):
    print('\n'*100)
    print('      '+'|'+'      '+'|')
    print('     '+board[7]+'|'+'   '+board[8]+'  '+'|'+board[9])
    print(' ------------------')
    print('      '+'|'+'      '+'|')
    print('     '+board[4]+'|'+'   '+board[5]+'  '+'|'+board[6])
    print('      '+'|'+'      '+'|')
    print(' ------------------')
    print('     '+board[1]+'|'+'   '+board[2]+'  '+'|'+board[3])
    print('      '+'|'+'      '+'|')
def player_chance():
    import random
    global rand
    print('1:Player 1 will play\n2:Player 2 will play')
    print('Processing toss.....')
    rand=random.randint(1,2)
    if rand==1:
        print(f'{rand}\nSo player 1 won the toss')
        return 1
    else:
        print(f'{rand}\nSo player 2 won the toss')
        return 2

def player_marker():
    global rand
    rand=player_chance()
    if rand==1:
        inpu=input(f'Player 1 please choose X or O:').upper()
        if inpu=='X':
            return('X','O')
        else:
            return('O','X')
    else:
        inpu=input(f'Player 2 please choose X or O:').upper()
        if inpu== 'X':
            return ('X','O')
        else:
            return ('O','X')

def win_check():
    global board
    stop=0
    if((board[1]=='X'and board[4]=='X' and board[7]=='X')or(board[2]=='X'and board[5]=='X' and board[8]=='X')or(board[3]=='X'and board[6]=='X' and board[9]=='X')or(board[1]=='X'and board[5]=='X' and board[9]=='X')or(board[3]=='X'and board[5]=='X' and board[7]=='X')or(board[1]=='X'and board[2]=='X' and board[3]=='X')or(board[4]=='X'and board[5]=='X' and board[6]=='X')or(board[7]=='X'and board[8]=='X' and board[9]=='X')):
        print('X wins')
        exit()
    elif((board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or (board[3] == 'O' and board[6]=='O' and board[9] == 'O') or (board[1] == 'O' and board[5] == 'O' and board[9] == 'O') or (board[3] == 'O' and board[5] == 'O' and board[7] == 'O') or (board[1] == 'O' and board[2] == 'O' and board[3] == 'O') or (board[4] == 'O' and board[5] == 'O' and board[6] == 'O') or (board[7] == 'O' and board[8] == 'O' and board[9]=='O')):
        print('O wins')
        exit()
    else:
        return stop
player_input()
