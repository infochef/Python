"""
Created on Sun Jul 21, 2024

@author: Somnath
@Description: Basic List Operations
"""

from rand import shuffle

li = [2, 3, 4, 2, 5, 3, 5, 7, 8, 3, 5, 9]


# Operation1 - Remove Duplicates from a list

def removeduplicates(li):
    new_list = []

    for ele in li:
        if ele not in new_list:
            new_list.append(ele)

    print('After removing the duplicates new list is: ', new_list)


# Operation1 - Check if given list is empty or not

def checklistcount(li):
    print(len(li))
    if len(li) > 1:
        print('Given list is not an empty list: ', li)
    else:
        print('Given list is an empty list: ', li)


# Operation3 - Remove Duplicates from a list

def copylist(li):
    # Method1 - Using slicing
    listslice = li[:]
    print('New copied list using slice operator is: ', listslice)

    # Method2 - Using extend()
    listex = []
    listex.extend(li)
    print('New copied list using extend function is: ', listex)

    # Method3 - Using list function
    listfunc = list(li)
    print('New copied list using list function is: ', listfunc)

    # Method4 - Using copy function
    listcopy = li.copy()
    print('New copied list using copy function is: ', listcopy)

    # Method1 - Using for loop
    listfor = [i for i in li]
    print('New copied list using for loop is: ', listfor)


# Operation4 - Program To Sort/Find The Words Greater Than A Certain Given Length From A List

def wordfinder():
    mylist = ['apple', 'cucumber', 'grapes', 'fruits', 'pinapple']

    for ele in mylist:
        if len(ele) > 6:
            print('{} element of the list is having words greater that a given length: '.format(ele))


# Operation4 - Program To Sort/Find The Words Greater Than A Certain Given Length From A sentence

def wordinsent():
    s = "The quick brown fox jumps over the lazy dog"
    newlist = []
    mylist = s.split(" ")

    for ele in mylist:
        if len(ele) > 3:
            newlist.append(ele)

    print('new list with all the words whose length is greater that 3 are: ', newlist)


# Operation4 - Compare two list and return true if the word matches

def comparetwolist():
    li1 = [1, 2, 3, 4, 5]
    li2 = [5, 6, 7, 8, 9]
    result = False

    for ele in li1:
        for ele2 in li2:
            if ele == ele2:
                print('True')
                break;

    print('Both the lists are not matching')


# Operation5 - Remove elements from a specified index

def removeele():
    li = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

    li = [x for (i, x) in enumerate(li) if i not in (0, 4, 5)]
    print(li)


# Operation6 - Remove even numbers from the list

def evenqw():
    listq = [7, 8, 120, 25, 44, 20, 27]

    # Iterate over a copy of the list
    for ele in listq[:]:
        if ele % 2 == 0:
            listq.remove(ele)

    print("List after removing even numbers:", listq)

# Operation7 - Reorder a list

def reorder():
    color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    shuffle(color)
    print(color)


removeduplicates(li)
checklistcount(li)
copylist(li)
wordfinder()
wordinsent()
comparetwolist()
removeele()
evenqw()
reorder()