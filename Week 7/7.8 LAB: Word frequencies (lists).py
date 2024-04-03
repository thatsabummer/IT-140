# Author: Caleb Smith
# Date: 10.16.2023


import csv

# Lab 7.8

# Write a program that first reads in the name of an input file and then reads the file
# using the csv.reader() method. The file contains a list of words separated by commas.
# Your program should output the words and their frequencies
# (the number of times each word appears in the file) without any duplicates.

# Get an input file

file = input()

# Create a list to store words from the file

word_list = []

# Open the user's input file as a csv

with open(str(file), 'r') as csvfile:
    user_file = csv.reader(csvfile, delimiter=',')

# Iterate over the file counting the number of times each word appears
  
    for row in user_file:
        for index in range(len(row)):
            if row[index] not in word_list:
              
                # Format and print the results
              
                print('{} {}'.format(row[index], row.count(row[index])))
                word_list.append(row[index])
