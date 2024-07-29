"""
Created on Sun Jul 28, 2024

@author: Somnath
@Description:  Python program to sort and get the maximum and minimum values of a dictionary.
"""

my_dict = {'x': 500, 'y': 5874, 'z': 560}

def find():

    # Method1 - Converting the dictionary value to list
    li = list(my_dict.values())
    print(li)
    li.sort()
    print('Maximum value of the dictionary is: ', li[-1])
    print('Minium value of the dictionary is: ', li[0])
    print(li)

    # Method2 - Using max and min function

    Max = max(my_dict.keys(), key = (lambda k:my_dict[k]))
    Min = min(my_dict.keys(), key = (lambda k:my_dict[k]))

    print('Maximum: ', my_dict[Max])
    print('Minimum: ', my_dict[Min])
    print(sorted(my_dict.keys()))
find()