# Read the file and store all the lines in list
# Reverse the list
# Write the list back to the file

with open('Alphabet.txt', 'r') as reader:
    content = reader.readlines() # ['Ant', 'Ball', 'Cat', 'Dog', 'Egg']
    reversed(content)  # ['Egg', 'Dog', 'cat', 'Ball', 'Ant']
    with open('Alphabet.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

