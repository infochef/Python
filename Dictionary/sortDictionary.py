"""
Created on Sun Jul 22, 2024

@author: Somnath
@Description: Script to sort (ascending and descending) a dictionary by value
"""

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def sortdict():

    values = sorted(d.values())
    print(values)
    keys = []

    for ele in values:
        temp = d[ele]
        keys.append(temp)
    print(keys)

    sorted_dict = dict(zip(keys, values))
    print('After sorting with values current dictionary is: ', sorted_dict)

sortdict()