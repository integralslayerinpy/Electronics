# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:07:24 2021

@author: monster
"""


def problem1():
    my_name="Haci Eren Karatas"
    a=my_name[0]
    return a
def problem2():
    my_name="Haci Eren Karatas"
    b=int(input("Enter a number: "))
    if (b>17 or b<0 ):
        return str(my_name[b%17])
    else:
        return str(my_name[b:b+1])
def problem3():
    my_name="Haci Eren Karatas"
    c=int(input("Enter first number: " ))
    d=int(input("Enter second number: "))
    if (c>17 or c<0) and (d>17 or d<0):
        e=c%17 
        r=d%17
        return str(my_name[e:r])
    else:
        return str(my_name[c:d])
    
def problem4():
    vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    u=str(input("Enter input: "))
    p=0
    for n in u:
        if n in vowels:
            p+=1
    return p

        
def problem5():
    my_id="200102002009"
    toplam=0
    for r in my_id:
        if len(my_id)>=0:
            toplam=toplam+int(r)
    return toplam


def problem6():
   h= int(input("Enter input "))
   for a in range(1,h):
       h=h*a
   return h
           
       

        
def problem7():
    numb = int(input("Enter a number:"))
    if numb % 7 == 0 and numb % 3 == 0:
        return True
    else:
        return False
    
    
def problem8():
    numb = int(input("Enter a number:"))
    if numb % 7 == 0 and numb % 3 == 0:
        return 3
    elif numb % 7 == 0:
        return 2
    elif numb % 3 == 0:
        return 1

def problem9():
    numb = int(input("Enter a number:"))
    flag = True
    if numb > 1:
        for i in range(2, numb):
            if numb % i == 0:
                flag = False
                break
    return flag

def problem10():
    numb=float(input("Enter a number: "))
    count=5
    eps=1e-10
    while True:
        count=(numb/count+count)/2
        if abs((count*count)-numb)<eps:
                 
           return count
       
    
        
         
     
   
    

    
        
 
        
    
    
    
    
            

               
              
    
        
        
           
           
    


            
      
            
        
            
    
        
   
        
  


    
    

    
    
    

  
    