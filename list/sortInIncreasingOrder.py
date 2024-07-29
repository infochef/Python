"""
Created on Sun Jul 21, 2024

@author: Somnath
@Description: Python program to get a list ,sorted in increasing order by the last element each tuple from list
@Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
@Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

def createlist():
    li = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(li)
    sort(li)
    print('sorted:', sort(li))
def last(n):
    return n[-1]

def sort(templist):
    return sorted(templist, key=last)

createlist()