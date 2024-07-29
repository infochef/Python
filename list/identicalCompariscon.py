"""
Created on Sun Jul 28, 2024

@author: Somnath
@Description: Python program to check whether two lists are circularly identical.

"""

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

def checklist():
    li1 = []
    for ele in list1:
        for ele in list2:
            if ele not in li1:
                li1.append(ele)
    print(li1)

    for ele in list1:
        for ele in list3:
            print('{} and {} are identical lists'.format(list1, list3))
    print('{} and {} are not identical lists'.format(list1, list3))

checklist()

