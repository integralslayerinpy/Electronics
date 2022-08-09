# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 11:51:20 2021

@author: monster
"""



def problem1(x):
    cards=['1','2','3','4','5','6','7','8','9','0','J','Q','K']
    for i in cards:
        if "K" in x:
            return True
        else:
            return False
def problem2(a,b,c,d):
    if (a<=b and a<=c)and(a<=d):
        return float(a)
    elif (b<=a and b<=c)and(b<=d):
        return float(b)
    elif (c<=a and c<=b)and c<=d:
        return float(c)
    elif (d<=a and d<=b)and d<=c:
        return float(d)
def problem3(a,b):
    if -1<a<0 and b<-1:
        a=-1
        return a
    if 0<a<1 and b>=0.5:
        a=1
        return a
    if a==int(a):
        return a
    if a>b:
        a=int(a)
        return a
    if a<b:
        a=int(a+1)
        return a
    
  
def problem4(radius,height,pi=3.1415):
    volume=pi*(radius**2)*height
    return volume
def problem5(radius,height,pi=3.1415):
    if (type(radius)==int or type(radius)==float) and (type(height)==float)and(type(pi)==float):
        volume=pi*(radius**2)*height
        return volume
    elif type(radius)==bool or type(radius)==str or radius==None:
        return -1
    elif type(height)==str or type(height)==bool or height==None:
        return -1
    elif type(pi)==str or type(pi)==bool or pi==None:
        return -1
    
   
def problem6(h):
    a=list(h)
    for i in a:
        if a.count(i)==1:
            return i
def problem7(t):
    a=list(t)
    b=sorted(t)
    if b==a:
        return True
    else:
        return False
def problem8(f):
    radikal=[]
    for characters in f:
        if characters in radikal:
            return False
        radikal.append(characters)
    return True
def problem9(row,column):
    if column<=row:
        if row==1 and column==1:
            return 1
        elif row>1 and column==1:
            return 3
        elif row>1 and column==row:
            return 2
    return problem9(row-1,column-1)+problem9(row-1,column)

        
    
    
def problem10(k,r):
    count=0
    for i in range(len(k)):
        for j in range(len(r)):
            if i==j and k[i]==r[j]:
                count+=1
    return count
    
    
    
    


    


            
        
    
            
            
            
   
 
    
    
    

    
        
        
            
      
    
 
        
        
    
    
        
    
        
    

    
        
        
    
        
        
            
          
            
            
            

    
    
    

        
    
    
   
        
       
    
   
    
            
    
        
    
    
        
    
  

    
        
    
    
    
        
        
    
    