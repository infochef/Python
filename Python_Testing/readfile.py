file = open("test.txt")

# Read all contents of file
# print(file.read())

# Read n number of characters by passing parameters
# print(file.read(5))

# Read one single line at a time readLine()
print(file.readline())
print(file.readline())

# Print line by line using readLine() method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# values = ['Apple', 'Butterfly', 'Camel', 'Dog', 'Elephant']
for line in file.readlines():
    print(line)

file.close()
