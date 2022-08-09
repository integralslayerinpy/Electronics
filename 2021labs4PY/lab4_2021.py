# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:44:33 2021

@author: monster
"""





def problem1(a,b):
    if b<0 or b>len(a):
        return None
    else:
        return a[b]
    
def problem2(c,d):
    if d<0 or d>len(c):
        return c
    else:
        del c[d]
        return c
    
def problem3(x,y):
    if y==True:
        x.sort()
        return x
    elif y==False:
        x.sort()
        x.reverse()
        return x
    
def problem4(l1,l2):
    count=0
    for i in l1:
        if i in l2:
            count+=1
    return count

def problem5(l,w):
    a=0
    for i in range(len(l)):
        a+= l[i] * w[i]
    toplam= sum(w)
    return float(a/toplam)

def problem6(a):
    if len(a)==1:
        return float(a[0][0])
    if len(a)==2 and len(a[0])!= len(a[1]):
        return None
    if len(a[0])==len(a[1])==2:
        d= a[0][0]*a[1][1]
        e= a[0][1]*a[1][0]
        return float(d-e)
    if len(a)==3 and (len(a[0])!=len(a[1]) or len(a[1])!=len(a[2]) or len(a[0])!=len(a[2])):
        return None
    if len(a)==3 and len(a[0])==len(a[1])==len(a[2]):
        f= a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1]
        g= a[0][2]*a[1][1]*a[2][0] + a[0][1]*a[1][0]*a[2][2] + a[0][0]*a[1][2]*a[2][1]
        return float(f-g)
    if len(a)==4 and (len(a[0])!=len(a[1]) or len(a[1])!=len(a[2]) or len(a[0])!=len(a[2]) or len(a[0])!=len(a[3]) or len(a[1])!=len(a[3]) or len(a[2])!=len(a[3])):
        return None
    if len(a)==4 and len(a[0])==len(a[1])==len(a[2])==len(a[3]):
        h= a[0][0]*a[1][1]*a[2][2]*a[3][3] + a[0][0]*a[1][3]*a[2][1]*a[3][2] + a[0][0]*a[1][2]*a[2][3]*a[3][1] + a[0][1]*a[1][3]*a[2][2]*a[3][0] + a[0][1]*a[1][0]*a[2][3]*a[3][2] + a[0][1]*a[1][2]*a[2][0]*a[3][3]
        i= a[0][2]*a[1][0]*a[2][1]*a[3][3] + a[0][2]*a[1][3]*a[2][0]*a[3][1] + a[0][2]*a[1][1]*a[2][3]*a[3][0] + a[0][3]*a[1][2]*a[2][1]*a[3][0] + a[0][3]*a[1][0]*a[2][2]*a[3][1] + a[0][3]*a[1][1]*a[2][0]*a[3][2]
        j= a[0][0]*a[1][3]*a[2][2]*a[3][1] + a[0][0]*a[1][1]*a[2][3]*a[3][2] + a[0][0]*a[1][2]*a[2][1]*a[3][3] + a[0][1]*a[1][0]*a[2][2]*a[3][3] + a[0][1]*a[1][3]*a[2][0]*a[3][2] + a[0][1]*a[1][2]*a[2][3]*a[3][0]
        k= a[0][2]*a[1][3]*a[2][1]*a[3][0] + a[0][2]*a[1][0]*a[2][3]*a[3][1] + a[0][2]*a[1][1]*a[2][0]*a[3][3] + a[0][3]*a[1][0]*a[2][1]*a[3][2] + a[0][3]*a[1][2]*a[2][0]*a[3][1] + a[0][3]*a[1][1]*a[2][2]*a[3][0]
        return float((h+i)-(j+k))

def problem7(accounts, source, lira, kurus):
     if source<0:
        return accounts
     if source>len(accounts)-1:
        return accounts
     if float(accounts[source])<(lira+(kurus/100)):
        return accounts
     else:
        accounts[source]= "{:.2f}".format(float(round(float(accounts[source])-(lira+kurus/100),2)))
        return accounts

        
    
def problem8(accounts, source, destination, lira, kurus, fee=False):
    if fee==True:
        if source==destination:
            return accounts
        if source<0 or destination<0 or source>len(accounts)-1 or destination>len(accounts)-1:
            return accounts
        if lira+kurus/100<10 and float(accounts[source])<lira+kurus/100 + round(((lira+kurus/100)*0.1/100),2):
            return accounts
        if lira+kurus/100>=10 and float(accounts[source])<lira+kurus/100 + round(((lira+kurus/100)*0.1/100),2):
            return accounts
        if lira+kurus/100<10 and float(accounts[source])>=lira+kurus/100 + round(((lira+kurus/100)*0.1/100),2):
            accounts[source]= str(float(round(float(accounts[source])-(lira+kurus/100 + round(((lira+kurus/100)*0.1/100),2)))))
            accounts[destination]= str(round(float(accounts[destination]) + (lira+kurus/100),2))
            return accounts
        if lira+kurus/100>=10 and float(accounts[source])>=lira+kurus/100 + round(((lira+kurus/100)*1/100),2):
            accounts[source]= str(round(float(accounts[source])-(lira+kurus/100 + round(((lira+kurus/100)*1/100),2)),2))
            accounts[destination]= str(round(float(accounts[destination]) + (lira+kurus/100),2))
            return accounts
    if fee==False:
        if source==destination:
            return accounts
        if source<0 or destination<0 or source>len(accounts)-1 or destination>len(accounts)-1:
            return accounts
        if float(accounts[source])<lira+kurus/100:
            return accounts
        if float(accounts[source])>=lira+kurus/100:
            accounts[source]= str(round(float(accounts[source]) - (lira+kurus/100),2))
            accounts[destination]= str(round(float(accounts[destination]) + (lira+kurus/100),2))
            return accounts
    

def problem9(x):
    c= [i for i in range(1,x+1)]
    index = 0
    if len(c) == 1:
        return 1
    while len(c)>1:
        index = (index + 6) % len(c)
        c.pop(index)
    return c[0]

def problem10(t):
    metin= ""
    for i in t:
        if t.count(i)==2:
            metin+=i
            return metin
    for i in t:
        if t.count(i)!=2:
            return None
    
        
       
    
    
    
        
    
            
            
            
            
        
                
        
        
        
        
        
        
                    
            
    
    

    
            
            
        
    


            
       
    
    
    
        

   
 

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
            
    
        
    
   
    
   
    
