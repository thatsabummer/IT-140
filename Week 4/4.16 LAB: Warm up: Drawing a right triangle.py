# Author: Caleb Smith
# Date: 09.21.2023

# 4-16 Lab: Draw a right triangle

#Get a character and a number of lines to print

triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')

# iterate over the number of lines printing the correct number of characters for the corresponding line number 

for i in range(triangle_height):
    print((triangle_char + ' ') * (i + 1))
