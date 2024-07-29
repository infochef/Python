"""
Created on Sun Jul 21, 2024

@author: Somnath
@Description: Python program to count the strings length is 2 or more and the first and last character are same
@Sample List : ['abc', 'xyz', 'aba', '1221']
@Expected Result : 2
"""


def createlist():
    li = []
    size = int(input('Enter the size of the list: '))

    for _ in range(size):
        temp = input('Enter the elements of the list: ')
        li.append(temp)

    countocc(li)


def countocc(templist):
    count = 0

    for ele in templist:
        if len(ele) > 1 and ele[0] == ele[-1]:
            print('Current iteration list item name is: ', ele)
            count += 1

    print('Count of the elements whose last and first characters are same: ', count)

createlist()