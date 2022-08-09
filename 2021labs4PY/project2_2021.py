# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 20:15:05 2021

@author: monster
"""

import random

def generate_random(row,column):
    generater=[]
    for i in range(row):
        generater.append([])
    for j in range(column):
        for x in generater:
            dict_keeper={
            'red': random.randint(0,255),
                  'green': random.randint(0,255),
                  'blue': random.randint(0,255)
                  }
            
            x.append(dict_keeper)
    return generater



    
    
    
    
    
    
    
    












def is_valid(img):
    control1=[]
    control2=[]
    for  i  in img:
        for c in i:
            a=list(c.values())
            control1.append(a)
    for  controller  in control1:
        for v in  controller:
            control2.append(v)
    for  scale in control2:
        if scale<0:
            return False
        if scale>255:
            return False
        if type(scale)!= int:
            return False
    return True



def read_from_file(filename):
    f=open("filename","r")
    for i in f:
        i=i.lstrip("#")
        lenner=len(i)
    return tuple(int(i[j:j+lenner//3],16) for j in range(0,lenner,lenner//3))
    
    
    











def write_to_file(img,filename):
    pass













def clear(img):
    for i in img:
        for j in i:
            j['green']=0
            j['red']=0
            j['blue']=0
    return None




def enhance(img,value,channel='rgb'):
    for e in img:
        for f in e:
            if channel=='b':
                f['blue']=round(f['blue']*value)
            if channel=='g':
                f['green']=round(f['green']*value)
            if channel=='r':
                f['red']=round(f['red']*value)
            if channel=='rgb':
                f['red']=round(f['red']*value)
                f['blue']=round(f['blue']*value)
                f['green']=round(f['green']*value)
            if channel=='rb':
                f['blue']=round(f['blue']*value)
                f['red']=round(f['red']*value)
            if channel=='rg':
                f['green']=round(f['green']*value)
                f['red']=round(f['red']*value)
            if channel=='gb':
                f['blue']=round(f['blue']*value)
                f['green']=round(f['green']*value)
    fix(img)
    return None
            
  




def set_value(img,value,channel='rgb'):
    for ist in img:
        for w in ist:
            if channel=='rg':
                w['red']=value
                w['green']=value
            if channel=='gb':
                w['green']=value
                w['blue']=value
            if channel =='rb':
                w['red']=value
                w['blue']=value
            if channel=='rgb':
                w['red']=value
                w['green']=value
            if channel=='r':
                w['red']=value
            if channel=='g':
                w['green']=value
            if channel=='b':
                w['blue']=value
    return None

            


def fix(img):
    for index in img:
        for iterr in index:
            if iterr['blue']>255:
                iterr['blue']=255
            if iterr['blue']<0:
                iterr['blue']=0
            if type (iterr['blue'])!=int:
                round(iterr['blue'])
            if iterr['green']>255:
                iterr['green']=255
            if iterr['green']<0:
                iterr['green']=0
            if type(iterr['green'])!=int:
                iterr['green']=round(iterr['green'])
            if iterr['red']>255:
                iterr['red']=255
            if iterr['red']<0:
                iterr['red']=0
            if type(iterr['red'])!=int:
                iterr['red']=round(iterr['red'])
    return None
                
            







def get_freq(img,channel='rgb',bin_size=16):
    pass

    
    
        
    


def rotate90(img):
    img2=[[""]*len(img) for i in range(len(img[0]))]
    for a in range(len(img)):
        for b in range(len(img[0])):
            img2[b][len(img) - a-1]=img[a][b]
    return img2

def rotate180(img):
    sist=[]
    for i in img:
        s=i[::-1]
        sist.append(s)
    return sist[::-1]


def rotate270(img):
    b=rotate90(img)
    c=rotate90(b)
    d=rotate90(c)
    return d





    
def mirror_x(img) :
    
    saver=[]
    saver1=[]
    for i in img:
        saver.append(i)
    for j in saver:
        x=j[::-1]
        saver1.append(x)
    img.clear()
    for z in saver1:
        img.append(z)
    return None


def mirror_y(img):
    saver2=[]
    for i in img:
        rust=i[::-1]
        saver2.append(rust)
    img.clear()
    for j in saver2:
        img.append(j)
    return None



    
def scale_up(img,N):
    upper=[]
    for i in img:
        for j in i:
            upper.extend(([j]*N))
            upper_split=[upper[k:k+N] for k in range(0,len(upper),N)]
            
    return upper_split




             
           
            
            

            
            












def grayscale(img,mode=1):
    for i in img:
        for x in i:
            if mode==4:
                modder4=int(x['red']*0.2627+x['green']*0.6780+x['blue']*0.0593)
                x['red']=modder4
                x['green']=modder4
                x['blue']=modder4
            if mode==3:
                modder3=int(x['red']*0.2126+x['green']*0.7152+x['blue']*0.0722)
                x['red']=modder3
                x['green']=modder3
                x['blue']=modder3
            if mode==2:
                modder2=int(x['red']*0.299+x['green']*0.587+x['blue']*0.114)
                x['red']=modder2
                x['green']=modder2
                x['blue']=modder2
            if mode==1:
                modder1=int(sum(x.values())/3)
                x['red']=modder1
                x['green']=modder1
                x['blue']=modder1
    fix(img)
    return None

                
def scale_down(img,N):
    pass

                
   



            
def apply_window(img,window):
    pass
     
        
    

    
    
    
            
            
            
            
            

    
    
    

    

        
    

            
    

    
    

 
        
        
            
    
   


            
                
                    
                
                    
                
                
                    
                    
                    
                
            
            
            
    







    
    
        
    
                
                
            
            
            
            
            
  
            



                
                
            
 
        
        
    


         
            
            




            

            
  

            
    




    
    
        
            
            
            
    
    
    
            
        
            
            
            

    
    
   
            
            

      
        
   
    
    

    
    
    
    
    
    