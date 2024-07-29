"""
Created on Sun Jul 27, 2024

@author: Somnath
@Description: Write a Python program to sum and multiply all the items in a dictionary.
"""

def sumitems():

    # Method1 - Using For Loop
    d = {}
    n = int(input('Enter the range of the dic: '))
    s = 0
    m = 1

    for i in range(1,n):
        k = input('Enter the key of the dic: ')
        v = int(input('Enter the value of the dic: '))
        d.update({k:v})
    print('Newly created dictionary is: ', d)

    for values in d.values():
        s = s + values
        m = m * values

    print('Sum of all the items in the dictionary is: ', s)
    print('Product of all the items in the dictionary is: ', m)

    # Method2 - Using sum function

    my_dict = {'data1': 100, 'data2': -54, 'data3': 247}

    result = sum(my_dict.values())
    print(result)

sumitems()
