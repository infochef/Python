"""
Created on Sun Jul 21, 2024

@author: Somnath
@Description: Python program to flatten a shallow list.
@Sample List : original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
@Expected Result : [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]
"""
import itertools
import functools
import operator

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

def flatenlist():

    # Method1 - Using For loop
    li = []
    for ele in original_list:
        for el in ele:
            li.append(el)

    print('using for loop: ', li)

    # Method2 - using extends function
    li2 = []
    for ele in original_list:
        li2.extend(ele)

    print('Using Extend Function: ', li2)

    # Method3 - Using list comprenshaion
    li3 = [item for ls in original_list for item in ls]
    print('using list comprehsion: ', li3)

    # Method4 - using itertools lib
    li4 = list(itertools.chain.from_iterable(original_list))
    print('Using itertools lib: ', li4)

    # Method5 - Using Functools
    li5 = functools.reduce(operator.iconcat, original_list, [])
    print('Using Functool lib: ', li5)

flatenlist()

