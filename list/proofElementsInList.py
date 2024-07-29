# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 00:49:52 2024

@author: somna
"""

def createlist():
    mylist = []
    size = int(input("Enter size of the list: "))
    
    for _ in range(size):
        temp = int(input("Enter the elements of the list: "))
        mylist.append(temp)
        
    print("All the elements present in list are: ", mylist)
    muleleinlist(mylist)
   
    
    
def muleleinlist(templist):
    
    total = 1
    for i in range(0, len(templist)):
        total = total * templist[i]
    
    print("Product of all the elements present in list are: ", total)
    
createlist()