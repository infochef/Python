""""
Created on Sun Jul 28, 2024

@author: Somnath
@Description:  Python program to remove duplicates from the dictionary.
"""

student_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    }
}

def removedup():
    student = {}
    for key, values  in student_data.items():
        if values not in student.values():
            student[key] = values
    print('After removing all the duplicates new dictionary is: ', student)

removedup()