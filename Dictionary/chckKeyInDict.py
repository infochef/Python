"""
Created on Sun Jul 27, 2024

@author: Somnath
@Description: Python script to check whether a given key already exists in a dictionary or remove a key from a
dictionary.
"""

sample_dict = {
    "name": "John Doe",
    "age": 30,
    "occupation": "Software Developer",
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {
        "street": "123 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zip": "62701"
    },
    "is_active": True
}

def chckkey():

    ele = input("Enter the key that you want to check: ")

    if ele in sample_dict:
        print('Key is already present in dictionary')
        print('Value for the key is ', sample_dict[ele])
    else:
        print('Key is not present in the dictionary')

def removekey():

    d = sample_dict.copy()
    d.pop('skills')
    print(d)
    del d['age']
    print(d)

chckkey()
removekey()
