# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:18:17 2021

@author: monster
"""


import random
class Person:
    
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
    
    def get_name(self):
        return str(self.name)+" "+str(self.lastname)
    def __str__(self):
        return str(self.name)+" "+str(self.lastname)
    def __lt__(self,other):
        if str(self.lastname)==str(other.lastname):
            if str(self.name)>str(other.name):
                return True
            else:
                return False
        if str(self.lastname)>str(self.lastname):
            return True
        else:
            return False
        

class Player(Person):
    genel_id=1
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
        self.power=( 
        random.randint(4,8)
        )
        self.id=Player.genel_id
        Player.genel_id +=1
        self.keeper=[]
        
    def get_power(self):
        return self.power
    def get_id(self,number):
        return self.id
    def add_to_points(self,x):
        self.x=x
        self.keeper.append(self.x)
    def get_points_detailed(self):
        return self.keeper
    def get_points(self):
        return sum(self.keeper)
    def set_team(self,t):
        self.t=t
    def get_team(self):
        return self.t
    def __lt__(self,other):
        self.other=other
        Player.__init__(name,lastname)
        other.get_points()=a
        self.name=b
        b.get_points()=c
        if a==c:
            if str(other.lastname)==str(self.lastname):
                if str(other.name)>str(self.name):
                    return True
                else:
                    return False
        if a>c:
            return True
        else:
            return False
    def reset(self):
        self.keeper.clear
        self.keeper.append(0)
        

class Manager(Person):
    genel_id2=1
    def __init__(self,name,lastname):
        self.influancer=[]
        self.name=name
        self.lastname=lastname
        self.id=Manager.genel_id2
        Manager.genel_id2 += 1
        self.lis=[]
        for i in range(4):
            a=(
                    random.randint(-10,10)
                    )
            self.lis.append(a)
            
            
        
            
    def get_id(self):
        return self.id
    def set_team(self,t):
        self.t=t
    def get_team(self):
        return self.t
    def get_influence_detailed(self):
        return self.lis
    def get_influence(self):
        return sum(self.lis)
    def __lt__(self,other):
        if other.lis==self.lis:
            if other.lastname==self.lastname:
                if self.name>other.name:
                    return True
                else:
                    return False
        if self.lis>other.lis:
            return True
        else:
            return False
    def reset(self):
        self.id=0
        self.lis.clear
        self.lis.append(0)
        

class Team:
    genel_id3=1
    def __init__(self,teamname,manager,players):
        self.teamname=teamname
        self.manager=manager
        self.players=players
        self.id=Team.genel_id3
        Team.genel_id3 +=1
        self.conc=0
        self.scorer=0
        self.winner=0
        self.loser=0
        self.fixtureren=[]
    
    def get_id(self):
        return self.id
    def get_name(self):
        return self.teamname
    def get_roster(self):
        return self.players
    def get_manager(self):
        return self.manager
    def __str__(self):
        return self.teamname
    def add_to_fixture(self,m):
        self.m=m
        self.fixtureren.append(self.m)
    def get_fixture(self):
        return self.fixtureren
    def get_conceded(self):
        return self.conceder
    def get_scored(self):
        return self.scorer
    def add_result(self,s):
        self.s=s
        self.conc +=s[1]
        self.scorer +=s[0]
        if s[0]>s[1]:
            self.winner += 1
        if s[1]>s[0]:
            self.loser +=1
    
    def get_wins(self):
        return self.winner
    def get_losses(self):
        return self.loser
    def __str__(self):
        return self.teamname
    def __lt__(self,other):
        a=(self.scorer-self.conc)
        b=(other.scorer-other.conc)
        if self.winner==other.winner:
            if a > b:
                return True
            else:
                return False
        if self.winner>other.winner:
            return True
        else:
            return False
        
class Match:
    def __init__(self,home_team,away_team,week_no):
        self.home_team=home_team
        self.away_team=away_team
        self.week_no=week_no
        self.result_home=0
        self.result_away=0
    def get_teams(self):
        return (self.home_team,self.away_team)
    def get_home_teams(self):
        return self.home_team
    def get_away_team(self):
        return self.away_team
    def play(self):
        c=(
                random.randint(-10,10)
                )
        d=(
                random.randint(-10,10)
                )
        self.result_home +=c
        self.result_away +=d
        
        
        
        
        
        for i in range(4):
            for j in range(5):
                a=(
                    random.randint(4,8)
                   )
                b=(
                    random.randint(-5,5)
                   )
            self.result_home += a
            self.result_home += b
        for k in range(4):
            for h in range(5):
                e=(
                        random.randint(4,8)
                        )
                z=(
                        random.randint(-5,5)
                        )
            self.result_away += e
            self.result_away += z
        if self.result_home==self.result_away:
            for p in range(5):
                ex=(
                        random.randint(4,8)
                        )
                xe=(
                        random.randint(-5,5)
                        )
            self.result_home += ex
            self.result_home +=xe
            for r in range(5):
                ern=(
                        random.randint(4,8)
                        )
                nre=(
                        random.randint(-5,5)
                        )
            self.result_away += ern
            self.result_away += nre
            
                
                
 
                
    def get_match_score(self):
        return (self.result_home,self.result_away)
    def is_played(self):
        if (self.result_home==0) and (self.result_away==0):
            return False
        else:
            return True
    def get_winner(self):
        if self.result_home > self.result_away:
            return self.home_team
        if self.result_away> self.home_team:
            return self.away_team
    def __str__(self):
        if (self.result_home==0) and (self.result_away==0):
            return str(self.home_team) + "vs." + str(self.away_team)
        else:
            return str(self.home_team) + "(" + str(self.result_home) + ")" + "vs." + "(" + str(self.result_away) + ")" + str(self.away_team)
        
        
        
        
class Season:
    keeper=[]
    phaser=[]
    f= open("players.txt", "r")
    lister= c.readlines()
    
    for i in lister:
        keeper.append(i.strip("\n").split(","))
    
    for i in keeper:
        for j in i:
            phaser.append(j)
            
    managent = []
    while len(phaser) > 5:
        cruch = phaser[:5]
        managent.append(cruch)
        phaser= phaser[5:]
    managent.append(phaser)
    
    teamer=[]
    err=[]
    a= open("teams.txt", "r")
    levi= a.readlines()
    
    for i in levi:
        teamer.append(i.strip("\n").split(","))
    
    for i in teamer:
        for j in i:
            err.append(j)
            
    
            
    
    extra= []
    gamer= []
    
    t= open("managers.txt", "r")
    liver= t.readlines()
    for i in liver:
        extra.append(i.strip("\n").split(","))
    
    for i in extra:
        for j in i:
            gamer.append(j)
            
    for z in range(18):
          managent.copy()[z].append(gamer[z])
          
    for a in range(18):
        managent.copy()[a].append(err[a])
    
    
    def _init_(self, teams, managers, players):
        self.teams = Season.levi
        self.managers= Season.liver
        self.players= Season.f
        
    def get_players(self):
        return Season.managent
    
    def get_managers(self):
        return Season.managent.copy()
    
    def get_teams(self):
        return Season.z
    def reset(self):
        pass
    def build_fixture(self):
        pass
    def get_week_fixture(week_no):
        pass
    def get_week_no(self):
        pass
    def play_week(self):
        pass
    def get_best_player(self):
        pass
    def get_best_manager(self):
        pass
    def get_most_scoring_team(self):
        pass
    def get_champion(self):
        pass
    
    
    
        
    
    
    
    
    
    

        
        

                
                
    
        
        
                
        
        
        
            
        
            
            
                
        
            
    
        

        
        
         
        
        
        
        
        
        
        
        
        
        
        
        
    
    
                
        
        
       
        
        
        
        
  
        
        
        
        
        
        
        
    
    
        



        

      
    



        
        
        
        
        
        
        
        
    


    
        
        
        
    