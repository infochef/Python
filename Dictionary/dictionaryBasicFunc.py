"""
Created on Sun Jul 22, 2024

@author: Somnath
@Description: Basic Operations
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


# Operation1 - Add keys to an existing dictionary

def addkey():
    tempdict = sample_dict.copy()
    print(tempdict)
    tempdict.update({'email_id': 'test.data@gmail.com'})
    tempdict['skills'].append('Java')
    tempdict['address']['zip'] = '62702'
    print(tempdict)
    items = list(tempdict.items())
    print(items)
    items.insert(2, ('email_id', 'test.data@gmail.com'))
    print(items)
    print(dict(items))


def concatenate():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    dic4 = {}

    # Method1 - using new variable and update operator
    dic4.update(dic1)
    dic4.update(dic2)
    dic4.update(dic3)
    print(dic4)

    # Method2 - using Arguments
    dic4 = {**dic1, **dic2, **dic3}
    print(dic4)

    # Method3 - using For Loop
    dic5 = {}
    for d in (dic1, dic2, dic3):
        dic5.update(d)
    print(dic5)


def iterdict():
    # Method1 - Using '.items'
    for k, v in sample_dict.items():
        print(k, ':', v)

    # Method2 - Using Keys of the dictionary
    for k in sample_dict.keys():
        print(k, ':', sample_dict[k])

    # Method3 - Using for loop
    for k in sample_dict.keys():
        print(k)
    for i in sample_dict.values():
        print(i)


addkey()
concatenate()
iterdict()
