# Author: Caleb Smith
# Date: 10.15.2023

# Lab 6.19
# Write a program that replaces words in a sentence.
# The input begins with word replacement pairs (original and replacement).
# The next line of input is the sentence where any word on the original list is replaced.

# Get word replacement pairs from the user
replacement_words = input().split()

# Make a dictionary to store original words and their replacements (word:new word)
new_dict = {}
for i in range(0, len(replacement_words), 2):
    original_word = replacement_words[i]
    new_word = replacement_words[i + 1]
    new_dict[original_word] = new_word

# Get the user's input & split it
sentence = input()
words = sentence.split()

# Make a new sentence with the replacement words
new_sentence = ' '.join(new_dict.get(word, word) for word in words)

# Print the new (updated) sentence
print(new_sentence)
