# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:56:21 2021

@author: monster
"""


def problem1():
    fah=int(input("Enter Fahrenheit degree: "))
    cel=(fah-32)*5.0/9.0
    return float(cel)
    
      
    
def problem2():
    cel=int(input("Enter Celsius degree: "))
    fah=(9.0*cel)/5.0+32
    return float(fah)
    
    




def problem3():
    hexa=int(input("Enter a number: "))
    if 1e6>= hexa >=1:
        total=2*hexa**2-hexa
        return int(total)
    
def problem4():
    n=int(input("Enter a number: "))
    x=2
    y=1
    lc=(1+5**0.5)/2
    lcs=(1-5**0.5)/2
    if n==0:
        return x
    elif n==1:
        return y
    else:
        z=(lc**n+lcs**n)
        return int(z)
   
 
        
        
   

            
        
        
    
   
        
        
def problem5():
    opp=str(input("Enter a string: "))
    s=len(opp)
    if s<= 100:
       r= opp[::-1]
       return r
       
    
        
   
    
   
    
def problem6():
   inp=str(input("Enter a string: "))
   unwchar='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
   #tup=list(unwchar)
   for i in unwchar:
       inp=inp.replace(i,"")
   return str(inp)

def problem7():
    target= int(input("Enter a number:"))
    adc =target
    s = ""
    while True:
        if target == 0:
            break
        else:
            if target < 0:
                target = -1*target
                s += str(target % 4)
                target = target // 4
            else:
                s += str(target % 4)
                target = target // 4

    if adc < 0:
        s = s + "-"

    return s[::-1]
        
            
     
     
         
            
           
         
     
     
      
   
        
      
     
        
       
        
def problem8():
    acikList = ["[", "{", "("]
    kapalList = ["]", "}", ")"]
    Brackets = input("Enter input: ")
    s = []
    for i in Brackets:
        if i in acikList:
            s.append(i)
        elif i in kapalList:
            red = kapalList.index(i)
            if (len(s) > 0) and (acikList[red] == s[len(s) - 1]):
                s.pop()
            else:
                return False
    if len(s) == 0:
        return True
        

        
    
    
    
  
        
    
    
def problem9():
    string=str(input("Enter a string: "))
    if len(string)<200:
        arc=string.split()
        adc=arc[-1]
        return len(adc)
    
    
    
    
def problem10():
    x= input("Enter the exit route: ")
    uzunluk = len(x)
    sayw= 0
    saye= 0
    sayn= 0
    says= 0
    
    for i in range(uzunluk):
        if x[i] == 'w':
            sayw +=1
        if x[i] == 'e':
            saye +=1
        if x[i] == 'n':
            sayn +=1
        if x[i] == 's':
            says +=1
            
    tt= sayw*-1 + saye*1
    yy= sayn*1 + says*-1
    
    targ= (tt**2 + yy**2)
    guess= 1
    eps= 1e-3
    
    while True:
        if abs(guess**2 - targ) < eps:
            break
        guess= guess -(guess**2 - targ)/(2*guess)
    return float(guess)


           
                
          
          
        
         
        
        
        
        
            
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
        
        
        
        
    

    
    
    
             
             
    

   


        
    
 
                

    
                
            
                
            
        

    

    
     
 
    
    
    
    
    
    
    
    

    
 
        