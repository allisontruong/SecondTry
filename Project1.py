"""
This is my first project which will be
documented later.
"""
# Task open a file from the web
# Iterate over the file
# Create a list of words from the file
# Iterate over the new list.
from urllib.request import urlopen

import sys


def fetch_words(f):
    """
    Fetch a list of words from a file
    :param f:  url address of an encoded file
    :return: nothing
    """
    #f = "http://icarus.cs.weber.edu/~hvalle/hafb/wasteland.txt"
    with urlopen(f) as story:
        story_words = []
        for line in story:
             line_rec = line.decode('utf-8').split()
             for word in line_rec:
                print(word)
                story_words.append((word))
    print("This file has: ", len(story_words), "words")

def main(f):
    #f = "http://icarus.cs.weber.edu/~hvalle/hafb/wasteland.txt"
    fetch_words(f)

if __name__ == '__main__':
    # f = "http://icarus.cs.weber.edu/~hvalle/hafb/wasteland.txt"
    url = sys.argv[1]
    main(url)
