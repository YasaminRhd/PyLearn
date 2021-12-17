import random
import time

CRED = '\033[91m'
CEND = '\033[0m'

CGREEN = '\33[32m' 
CgEND =  '\33[0m'



game =  [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

def showGameBoard():
    for row in game:
        for item in row:
            if item == 'X':
                print(CRED + 'X' + CEND, end=' ')
            elif item == 'O':
                print(CGREEN + 'O' + CgEND, end=' ')
            else:
                print('_', end=' ')            
        print()        

                        
def _input():
    row = int(input("from 0 to 2 select a row: "))
    col = int(input("from 0 to 2 select a column: "))
    return row, col
    
def input_validation(row, col, player):
    if 0 <= row <= 2 and 0 <= col <= 2:
        if game[row][col] == '_':
            if player == 1:
                game[row][col] = 'X' 
                return True
            else:
                game[row][col] = 'O' 
                print("Done!")
                return True 
        else:
            print('cell is not empty!')
            return False    
    else:
        print("try again!")  
        return False 
        
def check():
    #player 1
    if game[0][0] == 'X' and game[0][1] == 'X' and game[0][2] == 'X':
        print('player 1 wins!')
        end = time.time()
        print(end - start)
        exit()
    elif game[1][0] == 'X' and game[1][1] == 'X' and game[1][2] == 'X':
        print('player 1 wins!')
        end = time.time()
        print(end - start)
        exit()
    elif game[2][0] == 'X' and game[2][1] == 'X' and game[2][2] == 'X':
        print('player 1 wins!')
        end = time.time()
        print(end - start)
        exit()
    elif game[0][0] == 'X' and game[1][0] == 'X' and game[2][0] == 'X':
        print('player 1 wins!')
        end = time.time()
        print(end - start)        
        exit()
    elif game[0][1] == 'X' and game[1][1] == 'X' and game[2][1] == 'X':
        print('player 1 wins!')
        end = time.time()
        print(end - start)
        exit()
    elif game[0][2] == 'X' and game[1][2] == 'X' and game[2][2] == 'X':
        print('player 1 wins!')
        end = time.time()
        print(end - start)        
        exit()
    elif game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
        print('player 1 wins!')
        end = time.time()
        print(end - start)        
        exit()
           
    #player 2  
    elif game[0][0] == 'O' and game[0][1] == 'O' and game[0][2] == 'O':
        print('player 2 wins!')
        end = time.time()
        print(end - start)        
        exit()
    elif game[1][0] == 'O' and game[1][1] == 'O' and game[1][2] == 'O':
        print('player 2 wins!')
        end = time.time()
        print(end - start)        
        exit()
    elif game[2][0] == 'O' and game[2][1] == 'O' and game[2][2] == 'O':
        print('player 2 wins!')
        end = time.time()
        print(end - start)        
        exit()
    elif game[0][0] == 'O' and game[1][0] == 'O' and game[2][0] == 'O':
        print('player 2 wins!')
        end = time.time()
        print(end - start)        
        exit()
    elif game[0][1] == 'O' and game[1][1] == 'O' and game[2][1] == 'O':
        print('player 2 wins!')
        end = time.time()
        print(end - start)        
        exit()
    elif game[0][2] == 'O' and game[1][2] == 'O' and game[2][2] == 'O':
        print('player 2 wins!')
        end = time.time()
        print(end - start)        
        exit()
    elif game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
        print('player 2 wins!')
        end = time.time()
        print(end - start)        
        exit()
    else:
        cnt = 0
        flag = False 
        for row in game:
            if '_' not in row:
                cnt += 1
        if cnt == 3:
            flag = True
        else:
            flag = False            
        if flag:                
            print("The game equalised")
            end = time.time()
            print(end - start)             
            exit()   
        
        
start = time.time()       
print("how do you want to play the game?")
print("1.single player   2.double player")
howToPlay = int(input("your choice: "))

if howToPlay == 2:
    while True:
        showGameBoard()
        print('player 1: ')
        row, col = _input()
        input_validation(row, col, 1)
        check()
        
        showGameBoard()
        print('player 2: ')
        row, col = _input()
        input_validation(row, col, 2)
        check()
else: 
    while True:
        showGameBoard()
        print('player 1: ')

        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)
            if input_validation(row, col, 1):
                break
        check()
        
        showGameBoard()
        print('player 2: ')
        row, col = _input()
        input_validation(row, col, 2)
        check()
        