# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 00:30:47 2024

@author: somnath
"""

# =============================================================================
# method1 using for loop
# =============================================================================

def sumofelelist(templist):
    sum = 0
    
    for i in range(0, len(templist)):
        sum = sum + templist[i]
        
    print('Sum of all the elements present in list using for loop is: ', sum)
    
# =============================================================================
# method2 using builtin function loop
# =============================================================================


def sumofele(temp):
    
    total = sum(temp)
    print('Sum of all the elements present in list using builtin function is: ', total)
    
def createlist():
    mylist = []
    size = int(input("Enter list length: "))
    
    for _ in range(size):
        temp = int(input("Enter Elements of the list:"))
        mylist.append(temp)
    
    print("All the elements of the list are:", mylist)
    sumofelelist(mylist)
    sumofele(mylist)

createlist()


