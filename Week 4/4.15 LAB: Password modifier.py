# Author: Caleb Smith
# 09.21.2023

# 4.15 Lab - Password modifier

# Get an input string from the user

user_string = input()

# Change the 'i' to '!', 'a' to '@', 'm' to 'M', 'B' to '8', and 'o' to '.'

while 'i' or 'a' or "m" or 'B' or 'o' in user_string:
    if 'i' in user_string:
        user_string = user_string.replace('i', '!')
    if 'a' in user_string:
        user_string = user_string.replace('a', '@')
    if 'm' in user_string:
        user_string = user_string.replace('m', 'M')
    if 'B' in user_string:
        user_string = user_string.replace('B', '8')
    if 'o' in user_string:
        user_string = user_string.replace('o', '.')
    break

# Add 'q*s' to the string

password = user_string + 'q*s'

# Print the modified  string (password)

print(password)
