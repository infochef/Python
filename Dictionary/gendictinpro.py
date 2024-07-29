"""
Created on Sun Jul 27, 2024

@author: Somnath
@Description: Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
"""

def gendict():

    # Method1 - Using for and update function
    dic = {}
    num = int(input('Enter the range that you want: '))

    for ele in range(1, num):
        temp = ele * ele
        dic.update({ele:temp})
    print('Newly created dictionary is: ', dic)

   # Method2 - using only for loop

    # Prompt the user to input a number and store it in the variable 'n'.
    n = int(input("Input a number "))

    # Create an empty dictionary 'd' to store the square of numbers.
    d = dict()

    # Iterate through numbers from 1 to 'n' (inclusive).
    for x in range(1, n + 1):
        # Calculate the square of each number and store it in the dictionary 'd' with the number as the key.
        d[x] = x * x

    # Print the dictionary 'd' containing the squares of numbers from 1 to 'n'.
    print(d)

gendict()