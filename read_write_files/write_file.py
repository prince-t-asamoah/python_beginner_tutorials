# Example 1 - Text Files
with open('dog_breeds.txt', 'r') as reader:
    dog_breeds = reader.readlines()
    
with open('dog_breeds_reversed.txt', 'w') as file:
    # Option 1 - More pythonic
    file.writelines(reversed(dog_breeds))
    
    # Option 2
    for breed in reversed(dog_breeds):
        file.write(breed)
        
# Example 2 - Appending
with open('dog_breeds.txt', 'a') as file:
    file.write('\nBeagle')
    
    
# Example 3 - Read and Write
with open('dog_breeds.txt', 'r') as reader, open('dog_breeds_reversed.txt', 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))