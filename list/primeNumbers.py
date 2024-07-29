"""
Created on Sun Jul 21, 2024

@author: Somnath
@Description:  Check if each number is prime in a given list of numbers
"""

def createlist():
    li = []
    size = int(input('Enter the size of the list: '))

    for _ in range(size):
        temp = int(input('Enter the elements of the list: '))
        li.append(temp)

    print('All the elements of the list are: ', li)
    checkprime(li)

def checkprime(templist):

    for ele in templist:
        if ele >= 1:
            for i in range(2, ele):
                if ele % i == 0:
                    return False
            return True
    # print('{} is a list with all prime numbers'.format(templist))

createlist()
