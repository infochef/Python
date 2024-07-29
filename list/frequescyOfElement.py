"""

@author: Somnath
@Description: Python program to count the number of elements in a list within a specified range.

"""
from collections import Counter

my_list = [10, 20, 30, 40, 20, 50, 60, 40]

def countnum():

    # Method1 - Using dictionary
    dic = {}
    for ele in my_list:
        dic[ele] = dic.get(ele, 0) + 1
    print(dic)

    # Method2 - Using counter function

    li = Counter(my_list)
    print(li)

countnum()