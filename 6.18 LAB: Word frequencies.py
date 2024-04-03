# Author: Caleb Smith
# Date: 10.15.2023

# Lab 6.18
# Write a program that reads a list of words.
# Then, the program outputs those words and their frequencies.
# !!! case-sensitive

# Get input words from the user
word_input = input().split()

# Keep word frequencies in a dictionary (word:freq)
word_freq = {}

# Count the frequency of each word
for word in word_input:
    # Add one to word freq if the word appears
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Print the word frequencies
for word in word_input:
    print(word, word_freq[word])
