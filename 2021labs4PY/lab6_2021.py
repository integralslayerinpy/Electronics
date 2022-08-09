# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 22:20:22 2021

@author: monster
"""


import random
def problem1():
    class p1:
        def __init__(self,x):
            if type(x)==int:
                self.t=x
            if type(x)!=int:
                self.t=0
            
            
        def get_value(self):
            return self.t
        def set_value(self,x):
            if type(x)==int:
                self.b=x
    return p1


def problem2():
    class p2:
        def __init__(self,x,y):
            self.x=x
            self.y=y
        def get_area(self):
            return self.x*self.y
        def get_perimeter(self):
            return 2*(self.x+self.y)
    
    return p2

def problem3():
    grader=[]
    class Grades:
        def __init__ (self):
            return None
        def add_grade(self,x):
            self.x=x
            grader.append(x)
        def remove_grade(self,x):
            self.x=x
            grader.remove(x)
        def get_min(self):
            if len(grader)==0:
                return float(0)
            else:
                return float(min(grader))
        def get_max(self):
            if len(grader)==0:
                return float(0.0)
            else:
                return float(max(grader))
        def get_mean(self):
            if len(grader)==0:
                return float(0)
            else:
                return sum(grader)/len(grader)
        def get_median(self):
            if len(grader)==0:
                return float(0)
            if len(grader)==1:
                return grader[0]
            else:
                a=sorted(grader)
                b=len(grader)
                index=(b-1)//2
                if b%2:
                    return float(a[index])
                else:
                    return (a[index]+a[index+1])/2.0
    return Grades

def problem4():
    class Movie:
        def __init__(self,movie_name,director,year,rating=0.0,length=0):
            self.movie_name=movie_name
            self.director=director
            self.year=year
            self.rating=rating
            self.length=length
        def get_movie_name(self):
            return self.movie_name
        def get_director(self):
            return self.director
        def get_year(self):
            return self.year
        def get_rating(self):
            return self.rating
        def get_length(self):
            return self.length
        def set_rating(self,x=0.0):
            if 0.0<=x<=10.0:
                self.rating=x
        def set_length(self,y=0):
            if 0<=y<=500:
                self.length=y
        
                
            
    return Movie

def problem5():
    class MovieCatalog(problem4()):
        def __init__(self,filename):
            self.file=filename
            self.lst=[]
            nud=[]
            with open(filename) as f:
                lines=f.readlines()
                for row in lines:
                    nud.append(row.strip("\n").split(",")
                for i in nud:
                    self.lst.append(i)
                    
        
                    
        
        def add_movie(self,movie_name,director,year,rating=0.0,length=0.0):
            cataloger=[]
            cataloger.append(movie_name)
            cataloger.append(director)
            cataloger.append(year)
            cataloger.append(rating)
            cataloger.append(length)
            if cataloger not in self.lst:
                self.lst.append(cataloger)
            else:
                pass
        def remove_movie(self,movie_name):
            if movie_name in self.lst:
                self.lst.remove(movie_name)
            else:
                pass
        def get_oldest(self,year):
            pass
    pass

            
            
        
            
        


















def problem6():
    class Node:
        def __init__(self,x,y,z):
            self.x=x
            self.y=y
            self.z=z
        def get_node(self):
            return (self.x,self.y,self.z)
        def get_distance(self):
            return ((self.x**2)+(self.y**2)+(self.z**2))**0.5
        def __add__(self,other):
            c1=self.x + other.x
            c2=self.y + other.y
            c3=self.z + other.z
            return "<"+ str(c1) + ", " + str(c2) + ", " + str(c3) + ">"
        def __str__(self):
            return "<" + str(self.x)+", "+ str(self.y) + ", " + str(self.z) + ">"
        def __gt__(self,other):
            a=((self.x**2)+(self.y**2)+(self.z**2)**0.5)
            b=((other.x**2)+(other.y**2)+(other.z**2)**0.5)
            if a>b:
                return True
            else:
                return False
        def __ge__(self,other):
            a=((self.x**2)+(self.y**2)+(self.z**2)**0.5)
            b=((other.x**2)+(other.y**2)+(other.z**2)**0.5)
            if a>=b:
                return True
            else:
                return False
        def __lt__(self,other):
            a=((self.x**2)+(self.y**2)+(self.z**2)**0.5)
            b=((other.x**2)+(other.y**2)+(other.z**2)**0.5)
            if a<b:
                return True
            else:
                return False
        def __le__(self,other):
            a=((self.x**2)+(self.y**2)+(self.z**2)**0.5)
            b=((other.x**2)+(other.y**2)+(other.z**2)**0.5)
            if  a<=b:
                return True
            else:
                return False
            def __eq__(self,other):
                if a==b:
                    return True
                else:
                    return False
    return Node

def problem7():
    clouder=[]
    class NodeCloud(problem6()):
        def __init__(self,n):
            for i in range(n):
                tupler=(
                        random.randint(-20,20),
                        random.randint(-20,20),
                        random.randint(-20,20))
                clouder.append(tupler)
        def get_nodes(self):
            N=problem6()
            ninst1=N()
            tex=ninst1.get_node()
            clouder.append(tex)
            return clouder
        def get_outermost(self):
            maxer=[]
            for i in clouder:
                maxer.append((i[0]**2)+(i[1]**2)+(i[2]**2))
            t=max(maxer)
            for j in maxer:
                if maxer[j]==t:
                    return clouder[j]
        def add_node(self,x,y,z):
            self.x=x
            self.y=y
            self.z=z
            a=(self.x,self.y,self.z)
            clouder.append(a)
        def get_sum(self):
            s1=0
            s2=0
            s3=0
            for i in clouder:
                s1=i[0]+s1
                s2=i[1]+s2
                s3=i[2]+s3
            return (s1,s2,s3)
    return NodeCloud(problem6())
                
def problem8():
    class Encoder:
        pass
    pass

                        
                
        
        
                    
            
                
                
                
                
                
                
                
                
                    
                    
        
        
    
                
            
                
            
    









        




















            
            
            
            
            
        
        

            
            
            
            
        













    
        
        
        
            
    

    

                
                
                
        
                
                
                
                
             
                

            
                
        
        
                
                
                
            
            
            
            
        
        
            
            
        









    
    
    
            
    
    
        
        
        
    
    
    
        

    