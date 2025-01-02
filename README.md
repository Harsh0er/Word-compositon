Word Composition Problem Solution
Overview
This program solves the "Word Composition Problem" by identifying the longest and second-longest compound words from a list of words stored in input files. A compound word is one that can be created by concatenating other words in the same list.

Approach
The program processes the input files, reading the word list.
It checks each word to see if it can be composed of smaller words from the list.
The longest and second-longest compounded words are identified and displayed.
Requirements
Python 3.x
time module (for performance tracking)
Files
word_composition.py - Python script that processes the input and identifies compounded words.
Input_01.txt, Input_02.txt - Word list files (one word per line, all lowercase, sorted alphabetically).
README.md - Instructions for running the program.
Steps to Execute
Clone/download the repository.
Place your word list files in the same directory as word_composition.py.
Run the Python script with the command:
python word_composition.py
Output
The program will output the longest compound word, second-longest compound word, and the time taken to process each input file.
