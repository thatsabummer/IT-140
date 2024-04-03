# Author: Caleb Smith
# Date: 10.01.2023

# Write a program whose input is two integers and whose output is the two integers swapped

# define the swap values function

def swap_values(user_val1, user_val2):
    return user_val2, user_val1

# in truth, I don't know why we need this, but it doesn't work without it :)
if __name__ == '__main__':
  
    # get an input from the user for both int values 1 & 2
  
    user_val1 = (input())
    user_val2 = (input())
  
    # call the swap_values function and perform the operation, returning the new values
  
    swap_values(user_val1, user_val2)
  
    # print the new swapped valyes
    
    print(user_val2, user_val1)
