"""
Created on Sun Jul 27, 2024

@author: Somnath
@Description:  Python program to convert a list of characters into a string and find the index of a element
present in list
"""

s = ['a', 'b', 'c', 'd']
text = "Hello, world! Hello, Python!"

# Method1 - using for loop
def forloop():
    new = ""

    for ele in s:
        new += ele
    print(new)


#M Method2 - using Join function
def jo():

    n = ""
    print(n.join(s))

def findindex():
   v =  s.index('b')
   f = text.find('ji')
   print(v)
   print(f)

forloop()
jo()
findindex()
