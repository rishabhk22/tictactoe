
import numpy as np
import random

def new_board(): # make a new board
     new_board = np.full((3,3),'' ,dtype = str)
     return new_board

def init_game():
     # start and initalize the game
     board = new_board()
     player1_name = input("Enter player 1 name (X):")
     player2_name = input("Enter player 2 name (O):")

     player1_symbol = 'X'
     player2_symbol = 'O'

     #print(board)

     return board, player1_name, player2_name, player1_symbol, player2_symbol


#init_game()



def win_check(board):
    for row in board: # check rows for X
        if row[0]==row[1]==row[2]=='X':
            return("X won")
    for row in board:# check rows for O
        if row[0]==row[1]==row[2]=='O':
            return("O won")
    for col in range(3): # column rows for X
        if board[0][col]==board[1][col] == board[2][col]== 'X':
            return("X won")
    for col in range(3):# check columns for O
        if board[0][col]==board[1][col] == board[2][col]== 'O':
            return("O won")
    if board[0][0]==board[1][1] == board[2][2]== 'X': # check diagonal for X
            return("X won")
    if board[0][0]==board[1][1] == board[2][2]== 'O': # check diagonal for O
           return("O won")
    if board[0][2]==board[1][1] == board[2][0]== 'X': # check diagonal for X
            return("X won")
    if board[0][2]==board[1][1] == board[2][0]== 'O': # check diagonal for O
           return("O won")
    
    if np.all(board != ''):
            return ("Draw")
    
    return None

    #return result

#print(win_check(board))

def player_move(board, player_symbol,player_name):
     while True:
          try:
               print(f"{player_name}'s turn ({player_symbol}):")
               row= int(input(f"Enter the row (0-2)"))
               col= int(input(f"Enter the column (0-2)"))
               if board[row][col]!= '':
                    print("Please choose different position; this is already taken")
               else:
                    board[row][col] = player_symbol
                    break
          except ValueError:
               print("Invalid input! Please choose interger between 0-2")

def game():
     #start the game
     board, player1_name, player2_name, player1_symbol, player2_symbol = init_game()           
                    
     current_player_symbol = player1_symbol
     current_player_name = player1_name

     while True:
          
          print(board)
          #print("2343234323432")

          player_move(board, current_player_symbol, current_player_name)

          result = win_check(board)

          if result:
               print(board)
               print(result)
               break
          
          if current_player_symbol == player1_symbol:
               current_player_symbol = player2_symbol
               current_player_name = player2_name

          else:
               current_player_symbol = player1_symbol
               current_player_name = player1_name


game()
                


            