# List of names to be written to the file
names = ['Thabo', 'Bokang', 'Benjamin', 'Shayne',]

# Writing names to names.txt
with open('names.txt', 'w') as file:
    for name in names:
        file.write(name + '\n')

# Reading names from names.txt and printing them
with open('names.txt', 'r') as file:
    for line in file:
        print(line.strip())