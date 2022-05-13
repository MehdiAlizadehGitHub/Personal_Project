#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |   ')


# In[ ]:


def player_input():
    
    marker = ''
    
    #Ask player until he choose X or O
    
    while marker !='X' and marker !='O':
        marker=input('First Player, choose X or O: ')
    #Asign Player 2 the opposite marker
        player1 = marker
    
    if player1 == 'X':
        player2='O'
    else:
        player2='X'
        
    return (player1,player2)


# In[ ]:


def place_marker(board, marker, position):
    board[position]=marker


# In[ ]:


def win_check(board, mark):
    #WIN TIC TAC TOE?
    
    #All Rows check#The two diagonal#All Columns check
    return ((board[1]==board[2]==board[3]==mark) or 
    (board[4]==board[5]==board[6]==mark) or 
    (board[7]==board[8]==board[9]==mark) or
    
    #The two diagonal
    (board[1]==board[5]==board[9]==mark) or 
    (board[7]==board[5]==board[3]==mark) or
    
    #All Columns check
    (board[1]==board[4]==board[7]==mark) or 
    (board[2]==board[5]==board[8]==mark) or 
    (board[3]==board[6]==board[9]==mark))


# In[ ]:


import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# In[ ]:


def space_check(board, position):
    return board[position]== ' '


# In[ ]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[ ]:


def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position= int(input('Choose a position (1-9):'))
    return position


# In[ ]:


def replay():
    choice = input('Play again? Enter Yes or No :')
    return choice == 'Yes'


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn+' will go first')
    
    play_game = input('Ready to play? y or n? ')
    
    if play_game =='y':
        game_on = True
    else:
        game_on=False
       
    #Game Play

    while game_on:
        
        if turn == 'Player 1':
            #Show the board
            display_board(the_board)
            #Choose a position
            position = player_choice(the_board)
            #Place a marker on the position
            place_marker(the_board,player1_marker,position)
            #Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on=False
                else:
                    turn = "Player 2"
        #Player 1 Turn
                    
        else:
            #Show the board
            display_board(the_board)
            #Choose a position
            position = player_choice(the_board)
            #Place a marker on the position
            place_marker(the_board,player2_marker,position)
            #Check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on=False
                else:
                    turn = "Player 1"
        
        # Player2's turn.


    if not replay():
        break


# In[ ]:




