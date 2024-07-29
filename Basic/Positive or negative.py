def positive():
    num = float(input("Enter a number: "))
    if num > 0:
        print("Entered {0} number is positive".format(num))
    elif num==0:
        print("Entered {0} number is zero".format(num))
    elif num<0:
        print("Entered {0} number is negative".format(num))

positive()