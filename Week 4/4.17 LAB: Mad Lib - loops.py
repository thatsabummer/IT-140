# Author: Caleb Smith
# Date: 09.21.2023

# 4.17 Lab - Mad Lib (Loops)

# Get a string & an int from the user

user_input = input().split()
# Assign the inputs separately

word = user_input[0]
number = user_input[1]

# Iterate over the string until the user types 'quit'

while word != 'quit':
    print(f"Eating {number} {word} a day keeps the doctor away.")
    user_input = input().split()
    word = user_input[0]
    number = user_input[1]
