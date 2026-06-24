"""
Program: Heads Up

This program reads a list of words from a text file and can be used as the
starting point for a simple word guessing game.

Concepts practiced:
- Reading files
- Lists
- Strings
- Loops
- Helper functions
- Random choice
"""

# Code in Place IDE demo:
# Open this link and click Run to execute the program in the CIP IDE.
# https://codeinplace.stanford.edu/cip6/share/Mvcfu9sRHu4JcV1A52vq

import random

# Name of the file to read in
FILE_NAME = 'cswords.txt'


def get_words_from_file():
    """
    Reads the words from the text file and stores them in a list.
    Empty lines are skipped so the final list only contains real words.
    """
    lines = []
    with open(FILE_NAME) as f:
        for line in f:
            # Remove whitespace characters from the start and end of the line
            line = line.strip()

            # Only add the line if it has text
            if line != "":
                lines.append(line)

    return lines


def main():
    words = get_words_from_file()

    print("Heads Up")
    print("Words loaded:", len(words))

    if len(words) > 0:
        random_word = random.choice(words)
        print("Random word:", random_word)


if __name__ == '__main__':
    main()
