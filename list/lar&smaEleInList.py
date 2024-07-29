# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 00:30:47 2024

@author: somnath
"""


def createlist():
    mylist = []
    size = int(input("Enter the size of the list: "))

    for _ in range(size):
        temp = int(input("Enter the elements in the list: "))
        mylist.append(temp)

    print('All the elements present in the list are: ', mylist)
    larelelist(mylist)


def larelelist(templist):
    templist.sort()
    print('largest element of the list is: ', templist[-1])
    print('smallest element of the list is: ', templist[0])

    print('Largest element of the list is using builin function: ', max(templist))
    print('Largest element of the list is using builin function: ', min(templist))


createlist()