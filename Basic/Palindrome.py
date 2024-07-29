def palingdrome():
    num = int(input("Enter a number: "))
    # Input: 12321
    temp = num
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        print(remainder)
        reverse = (reverse * 10) + remainder
        print(reverse)
        temp = temp // 10
        print(temp)
    if num == reverse:
      print('Palindrome')
    else:
      print("Not Palindrome")
    # Output: Palindrome

palingdrome()