# http://www.laxcrossword.com/2013/11/la-times-crossword-answers-13-nov-13.html

from collections import defaultdict
from itertools import combinations, product
import re


class Letter(object):
    def __init__(self, character):
        self.character = character
        self.matches = []


class Word(object):
    def __init__(self, text):
        self.letters = [Letter(c) for c in text]
        
words = []

for line in open('words.txt'):
    text = re.sub('[^a-zA-Z]*', '', line)
    word = Word(text)
    words.append(word)


def link(a, b):
    a.matches.append(b)
    b.matches.append(a)


for word_a, word_b in combinations(words, 2):
    for letter_a, letter_b in product(word_a.letters, word_b.letters):
        if letter_a.character == letter_b.character:
            link(letter_a, letter_b)
        
def report():
    for a in words:
        print '#' * 20, a, '#' * 20

        for letter in a:
            print '-------', letter, '----------'
            for b in words:
                if a != b:
                    b_positions = re.findall(letter, b)
                    if b_positions:
                        print b

        print
        print
