"""
@author: Somnath
@Description: Python program to check whether a list contains a sublist.

"""

a = [2, 4, 3, 5, 7]
b = [4, 3]
c = [3, 7]

def checksublist():

    if len(b) > len(a):
        print('Given sub list is not present in main list as the size of the sub list is greater than main list')

    for i in range(len(a) - len(b)+1):
        window = a[i:i + len(b)]
        if window==b:
            print('Main list contains sub list')

checksublist()
