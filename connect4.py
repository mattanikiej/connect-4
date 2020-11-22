import numpy as np

#creates the board
board = np.array([['_', '_', '_', '_', '_', '_', '_'],
                 ['_', '_', '_', '_', '_', '_', '_'],
                 ['_', '_', '_', '_', '_', '_', '_'],
                 ['_', '_', '_', '_', '_', '_', '_'],
                 ['_', '_', '_', '_', '_', '_', '_'],
                 ['_', '_', '_', '_', '_', '_', '_']]) 

display = board[::-1]
four_in_a_row = False
turn = 1


def user_input():
    '''
    user inputs which column they want to put the puck in
    :return: int column number player chose
    '''
    player = 'A'
    if turn == 2:
        player = 'B'
    choice = int(input("Player {} select a column: ".format(player))) - 1
    return choice


def drop(): 
    '''
    checks to see which players turn it is and returns correct value
    :return: string value to drop in board
    '''
    if turn == 1:
        return 'A'
    if turn == 2: 
        return 'B'


def game_over():
    '''
    checks to see if game is over
    :return: True if over, False otherwise
    '''
    if up_and_down() == True:
        return True
    if side_by_side() == True:
        return True
    if diagonal() == True:
        return True
    return False


def up_and_down():
    '''
    checks for 4 in a row up and down
    :return: True if 4 pucks of the same value exist up and down, False otherwise
    '''
    count = 0
    
    #checks if player 1 won
    for col in range(7):
        for row in range(5):
            if board[row][col] == 'A' and board[row + 1][col] == 'A':
                count += 1
            if count == 3:
                print(display)
                print("Player A wins!")
                return True
        count = 0
    
    #checks if player 2 won
    for col in range(7):
        for row in range(5):
            if board[row][col] == 'B' and board[row + 1][col] == 'B':
                count += 1
            if count == 3:
                print(display)
                print("Player B wins!")
                return True
        count = 0
    return False 
            

def side_by_side():
    '''
    checks for 4 in a row side by side
    :return: True if 4 pucks of the same value exist side by side, False otherwise
    '''
    count = 0
    
    #checks if player 1 won
    for row in board:
        for i in range(6):
            if row[i] == 'A' and row[i + 1] == 'A':
                count += 1
            if count == 3:
                print(display)
                print("Player A wins!")
                return True
        count = 0
    
    #checks if player 2 won
    for row in board:
        for i in range(6):
            if row[i] == 'B' and row[i + 1] == 'B':
                count += 1
            if count == 3:
                print(display)
                print("Player B wins!")
                return True
        count = 0
    return False 

def diagonal():
    '''
    checks for 4 in a row diagonally
    :return: True if 4 pucks of the same value exist diagonally, False otherwise
    '''
    # top to bottom diagonal
    for i in range(4):
        for j in range(3,6):
           
            if board[i][j] == 'A' and board[i+1][j-1] == 'A' and board[i+2][j-2] == 'A' and board[i+3][j-3] == 'A':
                print(display)
                print("Player A wins!")
                return True
            
            if board[i][j] == 'B' and board[i+1][j-1] == 'B' and board[i+2][j-2] == 'B' and board[i+3][j-3] == 'B':
                print(display)
                print("Player B wins!")
                return True
        
    # bottom to top diagonal
    for i in range(4):
        for j in range(3):
            
            if board[i][j] == 'A' and board[i+1][j+1] == 'A' and board[i+2][j+2] == 'A' and board[i+3][j+3] == 'A':
                print(display)
                print("Player A wins!")
                return True
            
            if board[i][j] == 'B' and board[i+1][j+1] == 'B' and board[i+2][j+2] == 'B' and board[i+3][j+3] == 'B':
                print(display)
                print("Player B wins!")
                return True
            
    return False


if __name__ == '__main__':
    #game runs until 4 in a row is true
    while four_in_a_row == False: #checks to see of the game is over
        print(display) #shows board to players
        choice = user_input() #user selects col 1-7
                
        for row in board:
            if row[choice] == 'A' or row[choice] == 'B':
                continue
            if row[choice] == '_':
                row[choice] = drop()
                if row[choice] == 'A': #changes player turn
                    turn = 2
                else:
                    turn = 1
            break
        four_in_a_row = game_over()