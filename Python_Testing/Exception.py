ItemsInCart = 0
# 2 items will be added to the cart

if ItemsInCart != 2:  # raise Exception('Products cart count not matching')
    pass  # If the control goes to if loop by using 'pass' keyword we tell compiler to do nothing if pass keyword is
    # present

# assert (ItemsInCart == 2)
assert (ItemsInCart == 0)

# try, except(catch)
try:
    with open('lifelong.txt', 'r') as reader:
        reader.read()

except Exception as e:  # In python we are having except in place of catch. In Java, C# or other languages we
    # are having catch but in python we are having except instead of catch
    print("Somehow I reached this block because there is a failure in try block")
    print(e)

finally:
    print('Cleaning up resources')