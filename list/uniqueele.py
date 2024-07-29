"""

@author: Somnath
@Description: Python program to get unique values from a list.

"""

my_list = [10, 20, 30, 40, 20, 50, 60, 40]
li = []

def unique():

    # Method1 - Using For Loop
    for ele in my_list:
        if ele not in li:
            li.append(ele)
    print('New List is: ', li)

    # Method2 - Using set

    lis = set(my_list)
    # print(lis)
    my = list(lis)
    print(my)

unique()