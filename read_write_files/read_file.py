# Example 1
reader = open('dog_breeds.txt')
try:
    # Further file processing goes here
    pass
finally:
    reader.close()

# Example 2
with open('dog_breeds.txt') as reader:
    # Further file processing goes here
    pass

# File Types
# Example 3
file = open('dog_breeds.txt')
print(type(file)) # <class '_io.TextIOWrapper'>

# Example 4
file = open('dog_breeds.txt', 'rb')
print(type(file)) # <class '_io.BufferedReader'>

# Example 5
file = open('dog_breeds.txt', 'wb')
print(type(file)) # <class '_io.BufferedWriter'>

# Example 6
file = open('dog_breeds.txt', 'rb', buffering=0)
print(type(file)) # <class '_io.FileIO'>

# Example 7
with open('dog_breeds.txt', 'r') as reader:
   # Read & print the entire file
   print(reader.read())
    # Pug
    # Jack Russell Terrier
    # English Springer Spaniel
    # German Shepherd
    # Staffordshire Bull Terrier
    # Cavalier King Charles Spaniel
    # Golden Retriever
    # West Highland White Terrier
    # Boxer
    # Border Terrier

# Example 8
with open('dog_breeds.txt', 'r') as reader:
    # Read & print the first 5 characters of the line 5 times
    print(reader.readline(5))
    # Notice that line is greater than the 5 chars and continues
    # down the line, reading 5 chars each time until the end of the
    # line and then "wraps" around
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))
    # Pug

    # Jack
    # Russe
    # ll Te
    # rrier
    
    
# Example 9
f = open('dog_breeds.txt')
f.readlines()  # Returns a list object

# Example 10
f = open('dog_breeds.txt')
list(f)

# Example 11
with open('dog_breeds.txt', 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()

# Example 12
with open('dog_breeds.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')

# Example 13
with open('dog_breeds.txt', 'r') as reader:
    # Read and print the entire file line by line
    for line in reader:
        print(line, end='')
        
# Example 14
with open('./read_write_files/dog_breeds.txt', 'rb') as file:
    print(file.readline())

# Example 15
with open('./read_write_files/jack_russell.jpg', 'rb') as file:
    print(file.read(1))
    print(file.read(3))
    print(file.read(2))
    print(file.read(1))
    print(file.read(1))
    
    