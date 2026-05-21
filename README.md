# Bookbot

## Project Overview:
- A Python command-line program that analyzes a text file and generates a simple report. It counts the total number of words in the book and counts how many times each alphabetical character appears.

## Description:
 This project reads a `.txt` book file, processes the text, and prints a report to the terminal. The report includes:
    - The path of the book being analyzed
    - The total word count
    - A sorted character frequency count from greatest to least
    - Only alphabetical characters are included in the final character report

## How to run:
- From the project folder, type:
    python3 main.py <path_to_book>

- Example:
    python3 main.py books/mobydick.txt

## Files:
  main.py

This file controls the main program. It:

  - Imports the required functions
  - Reads the command-line argument using sys.argv
  - Opens and reads the book file
  - Calls the word count and character count functions
  - Prints the final report

    
  stats.py

This file contains the helper functions used to analyze the book text. It includes functions for:

  - Counting words
  - Counting characters
  - Sorting the character counts from greatest to least
Features:
  - Reads any .txt file passed through the command line
  - Counts total words
  - Counts each character
  - Sorts characters by frequency
  - Skips non-alphabetical characters in the final report
  - Uses a clean command-line interface
Requirements:

  - Python 3 verison or highier

No external libraries are required.

Author
  - Jesus F.
