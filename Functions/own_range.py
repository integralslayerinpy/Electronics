# -*- coding: utf-8 -*-
"""
own classic range function 

"""

def my_range(start, stop):
    mainList = []
    loop4 = stop - start
    j = 0
    
    while (loop4) >= 0:
        mainList.append(0)
        loop4 = loop4 - 1
    for i in mainList:
        mainList[j] = start + j
        j += 1
    mainList.pop()
    return (tuple(mainList))

"""
start - stop - step structere in range function
for only positive step

"""

def ft_range(start,end,step=1):
    mainList = [start]
    while start < end:
        start += step
        mainList.append(start)
    mainList.pop()
    return tuple(mainList)

"""
my reverse range function with start - stop - step

"""

def ft_rrange(start,end,step=1):
    mainList = [start]
    while start > end:
        start += step
        mainList.append(start)
    mainList.pop()
    return tuple(mainList)
    
        
            
        
    