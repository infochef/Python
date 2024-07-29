def anagram():
    str1 = input('Enter the 1st string:')
    str2 = input('Enter the 2nd string:')
    print(sorted(str1))
    print(sorted(str2))
    if(sorted(str1) == sorted(str2)):
        print('anagram')
    else:
        print('Not anagram')

anagram()