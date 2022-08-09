# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 23:05:52 2021

@author: monster
"""




def problem1(x,y):
    l1=[]
    l2=[]
    if y<=0 :
        return l2
       
    if y>0:
        for i in x:
            if x.count(i)==y:
                l1.append(i)
                a=set(l1)
                b=list(a)
        return b
    
def problem2(null):
    a=[]
    if len(null)==0:
        return 0
    for i in null.values():
        a.append(i)
    if len(a)%2==1:
        return a[int((len(a)-1)/2)]
    elif len(a)%2==0:
        return int(sum(a)/len(a))
    






def problem3(x):
    l=[]
    d1={}
    d2={}
    d3={}
    d4={}
    f=open(x,"r")
    data=f.readlines()
    
    for i in data:
        fresh_data=i.strip().split(", ")
        l.append(fresh_data)
    for j in l:
        pass
    
        
       
        
    
    

    
    








def problem4(holder,termer):
    grades = {"AA":4.0,"BA":3.5,"BB":3.0,"CB":2.5, "CC":2.0, "DC":1.5,"DD":1.0,"FF":0, "NA":"NA"}
    count1=0
    count2=0
    for i in range(len(holder)):
        if holder[i]["term"]==termer:
            if holder[i]["grade"]!=None:
                if holder[i]["grade"]=="NA":
                    count1 += 0
                    count2 += 0
                else:
                    count1 += holder[i]["credit"]*grades[holder[i]["grade"]]
                    count2 += holder[i]["credit"]
            else:
                count1 += 0
                count2 += 0
        if holder[i]==None and all(holder[i]["term"] != termer):
            return 0
    if count2==0:
        return 0
    else:
        return int(count1/count2*100)/100
                
    
 

                
                    
                




















def problem5(func,numb):
    a=0
    for index in range(numb+1):
        for cnt in str(index):
            if cnt=="1":
                a+=1
    if func(numb)==a:
        return True
    else:
        return False
    
            
        
    
    

































def problem6(tt):
    tt.lower()
    list1=[]
    for i in range(len(tt)-1,-1,-1):
        for j in range(len(list1)):
                list1.append(tt[i]+list1[j])
        list1.append(tt[i])
        list2=sorted(list1)
        list3=set(list2)
        list4=list(list3)
    return list4

        
    



def problem7():
    pass











def problem8(m1,m2):
    a=[]
    b=[]
    if m1==m2:
        return True
    for i in m1:
        for j in m1[i]:
            a.append(j) 
#            if a==m2:
#                return True
#    for z in m1:
    pass

        
        
            

   
    
    
    
def problem9(stri):
    ne_dic={}
    stri=""
    for i in stri:
        if i in ne_dic:
            ne_dic[i]+=1
        else:
            ne_dic[i]=1
    a=list(ne_dic.keys())
    b=list(ne_dic.values())
    for j in a:
        for z in b:
            pass
        
            
        
    

        


            
        
    






def problem10(inte):
    inte.sort()
    mtd=[j for j in range(inte[0],inte[-1]+1) if j not in inte  ]
    mpt=[j for j in range(inte[0],inte[-1]+1) if j in inte]
    for i in mtd:
            return i
    for k in mpt:
        return inte[-1] +1
    
    


    
    
    
            
        
        


            
    
    
  
        
  
        

    

            
        
    
    
        
    

            
           
        
                
        