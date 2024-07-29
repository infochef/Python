""""
Created on Sun Jul 28, 2024

@author: Somnath
@Description:  Python program to combine two dictionary by adding values for common keys.
"""
from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
# Required output - ({'a': 400, 'b': 400, 'd': 400, 'c': 300})

def addsameele():

    # Method1 - Using for loop

    for key, value in d2.items():
        if key in d1.keys():
            d1[key] = d1[key] + d2[key]
        else:
            d1[key] = value
    print('After iterating over the dictionary the new dictionary is: ', d1)

    # Method2 - Using counter function

    d = Counter(d1) + Counter(d2)
    print(d)
    
addsameele()