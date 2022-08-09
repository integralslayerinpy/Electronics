# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 19:28:30 2021

@author: monster
"""

import random

def generate(row,column):
    a=[[i+j*row for i in range(row)]for j in range(column)]
    return a
b=generate(3,3)

def get_board_size(board):
    return (len(board),len(board[0]))


    
def shuffle(board,times=20):
    
    possible_movements=["R","L","U","D"]
    chosen_movements=[]
    time_count=times
    while time_count>0:
        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[i][j]==0:
                    chosen=random.choice(possible_movements)
                    if chosen=="L" and board[i][j]==0:
                        board[i][j]=[i][j-1]
                        board[i][j-1]=0
                elif chosen=="R" and board[i][j]==0:
                    if len(board[0]-1)-j==0:
                        board[i][j]=board[i][0]
                        board[i][0]
                    else:
                        board[i][j]=board[i][j+1]
                elif chosen=="U" and board[i][j]==0:
                    board[i][j]=board[i-1][j]
                    board[i-1][j]=0
                elif chosen =="D" and board[i][j]==0:
                    if i>(len(board[0])-2):
                        board[i][j]=board[(len(board[0])-1)][j]
                        board[(len(board[0])-1)][j]=0
                    else:
                        board[i][j]=board[i+1][j]
                        board[i+1][j]=0
                time_count=time_count-1
                chosen_movements.append(chosen)
    return ''.join(chosen_movements)

                    
                

      
    
def reset(board):
    for i in range(len(board)):
        for k in range(len(board[0])):
            board[i][k]=i*len(board)+k
    return None

    
    
     
   


 
    
    
    
        
   

    

    




def is_valid(board):
    d=[]
    if (len(board)*len(board))>board[-1][-1]:
        for t in range(0,len(board)**2):
            d.append(t)
            for t in d:
                if d.count(t)==1:
                    return True
                else:
                    return False
    else:
        return False
    
            
            
        
    
    
def is_solved(board):

            pass
            
    
 
    
        
   
            
            
            
    
  




def rotate(board):
    pass
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j],end=" ")
        print()
def move_right(board):
    for i in board:
        for j in range(len(i)-1):
            if i[j]==0:
                i[j]=i[j+1]
                i[j+1]=0
                return 1
    return 0
def move_left(board):
    for i in board:
        for j in range(1,len(i)):
            if i[j]==0:
                i[j]=i[j-1]
                i[j-1]=0
                return 1
    return 0
def move_down(board):
    for i in range(len(board)-1):
        for j in range(len(board[i])):
            if board[i][j]==0:
                board[i][j]=[i+1][j]
                board[i+1][j]=0
                return 1
    return 0
def move_up(board):
    for i in range(1,len(board)):
        for j in range(len(board[i])):
            if board[i][j]==0:
                board[i][j]=board[i-1][j]
                board[i-1][j]=0
                return 1
    return 0

def move_random(board):
    pass

 
        
        
        
        
        
    
                
            
    
        
    
    

                
            
        

def move(board,moves):
    x=0
    for i in moves:
        if i=="U" or i=="u":
            if move_up(board)==1:
                x=x+1
        if i=="r" or i=="R":
            if move_right(board)==1:
                x=x+1
        if i=="D" or i=="d":
            if move_down(board)==1:
                x=x+1
        if i=="L" or i=="l":
            if move_left(board)==1:
                x=x+1
    return x




def play(board,moves):
    isvalid=is_valid(board)
    if isvalid== False:
        return -2
    else:
        issolved=is_solved
        if issolved == True:
            return 0
        else:
            m=move(board,moves)
            issolved=is_solved(board)
            if issolved== True:
                return m
            else:
                return -1
            
            

        
                
        
        
    
    
                
    
            

    
    

    
    
    
    
   

    
   
            
            
    
    
    
  
        
        
        



    
    
    
    
        
        
    
    
        
    
    
    
    

        
        
        
        
        
    
    

            
    

