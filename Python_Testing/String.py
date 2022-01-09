stri = "Python.programming.language"
str1 = "Python"
str2 = " Unique  "

print("*************************************")
print(stri[1])  # y

print("*************************************")
print(stri[0])  # P

print("*************************************")
# syntax - str [0 to n-1] where n will start from 0 and n will be total number of characters present in the string
print(stri[0:6])  # Python

print("*************************************")
print(stri[1:5])  # ytho

print("*************************************")
print(stri[:5])  # Pytho

print("*************************************")
print(stri[1:])  # ythonprogramminglanguage

print("*************************************")
print(stri[:])

print("*************************************")
print(str1 in stri)
print(str2 in stri)

print("*************************************")
var = stri.split(".")  # use to separate two words or strings
print(var)
print(var[0])

print("*************************************")
obj = str2.strip()  # use to remove white spaces
print(str2)
print(obj)
print(str2.lstrip())  # use to remove white spaces only from left
print(str2.rstrip())  # use to remove white spaces only from right
