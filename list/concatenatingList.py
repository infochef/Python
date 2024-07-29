"""
@author: Somnath
@Description: Python program to check whether a list contains a sublist.
@Sample list : ['p', 'q']
@n =5
@Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""

def createlist():

    li = []
    size = int(input('Enter the size of the list: '))

    for _ in range(size):
        temp = input('Enter the elements of the list: ')
        li.append(temp)

    print('The new list is: ', li)
    concat(li)

def concat(templist):
    new_list = []
    new_list1 = []
    length = int(input('Enter the length of the list: '))

    for i in range(length):
        for ele in templist:
            new_list.append('{}{}'.format(ele,i))
            new_list1.extend(ele)
    print('After concatination the new list is: ', new_list)
    print('After concatination the new list is: ', new_list1)

createlist()
