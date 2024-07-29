def primeNumber():
    num = int(input('Enter the number:'))
    flag=False
    if num > 1:
        for i in range(2, num):
            print(i)
            if (num%i)==0:
                flag=True
                break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

primeNumber()