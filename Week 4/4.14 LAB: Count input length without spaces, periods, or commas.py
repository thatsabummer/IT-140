# Author: Caleb Smith
# Date: 09.21.2023

# 4.14 Lab - Count input length (without spaces, periods, or commas)
# Get an input string from the user

user_string = input()

# Remove the ignored characters

while ' ' or '.' or "," in user_string:
    if " " in user_string:
        user_string = user_string.replace(' ', '')
    if "." in user_string:
        user_string = user_string.replace('.', '')
    if "," in user_string:
        user_string = user_string.replace(',', '')
    break
  
# Calculate the new string length

string_length = len(user_string)

# Display the string length

print(string_length)
