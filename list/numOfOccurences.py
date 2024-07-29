"""
Created on Sun Jul 21, 2024

@author: Somnath
@Description: Count Occurrences of an element in a list
"""

from collections import Counter


def createlist():
    mylist = []
    size = int(input('Enter the size of the list: '))

    for _ in range(size):
        temp = int(input('Enter the elements of the list: '))
        mylist.append(temp)

    print('All the elements of the list are: ', mylist)
    # countele(mylist)
    # coufunc(mylist)
    # counterfunc(mylist)
    allelefunc(mylist)


# Method1 - Using For loop
def countele(templist):
    count = 0
    x = int(input('Enter the element for which you want to know the number of occurances: '))

    for ele in templist:
        if (ele == x):
            count = count + 1
    print('{} has occured {} times'.format(x, count))


# Method2 - Using count function present in collection
def coufunc(temp):
    x = int(input('Enter the element for which you want to know the number of occurances: '))
    print('{} has occured {} times'.format(x, temp.count(x)))


# Method3 - Using counter function present in collection
def counterfunc(temp):
    x = int(input('Enter the element for which you want to know the number of occurances: '))
    dic = Counter(temp)

    print('{} has occured {} times'.format(x, dic[x]))


# Approach2 - Count occurances for all the elements
# Method1 - Using counter function
def allelefunc(temp):
    dic = Counter(temp)

    for item in dic:
        print(item, '-', dic[item])

    print('All has occured {} times'.format(dic))
