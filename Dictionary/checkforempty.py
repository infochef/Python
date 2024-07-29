""""
Created on Sun Jul 28, 2024

@author: Somnath
@Description:  Python program to check if a dictionary is empty or not.
"""

my_dict = {'x': 500, 'y': 5874, 'z': 560}

def checkdic():

    # Method1 - Using If statement
    print(len(my_dict))
    if len(my_dict)>0:
        print('{} dictionary is not empty'.format(my_dict))
    else:
        print('{} dictionary is  empty'.format(my_dict))

    # Method2 - Using bool function
    # The 'bool()' function returns False for an empty dictionary, so if it's not empty, the condition is True.
    if not bool(my_dict):
        print('Dictionary is Empty')

checkdic()