# http://www.laxcrossword.com/2013/11/la-times-crossword-answers-13-nov-13.html
from __future__ import print_function

from collections import defaultdict
from itertools import combinations, product
import re


class Letter(object):
    def __init__(self, character, word):
        self.character = character
        self.word = word
        self.matches = []

    def __repr__(self):
        return 'Letter({}, {})'.format(self.character, self.word)


class Word(object):
    def __init__(self, text):
        self.text = text
        self.letters = [Letter(c, self) for c in text]

    def __str__(self):
        return self.text
        
words = []

for line in open('words.txt'):
    text = re.sub('[^a-zA-Z]*', '', line)
    word = Word(text)
    words.append(word)


def link(a, b):
    a.matches.append(b)
    b.matches.append(a)


def header(*args, **kwargs):
    char = kwargs.get('char', '#')
    marker = char * 20
    print_args = (marker,) + args + (marker,)
    print()
    print(*print_args)


for word_a, word_b in combinations(words, 2):
    for letter_a, letter_b in product(word_a.letters, word_b.letters):
        if letter_a.character == letter_b.character:
            link(letter_a, letter_b)
        

def ngrams(seq, min_n, max_n=None):
    if max_n is None:
        max_n = min_n

    seqlen = len(seq)
    for i in xrange(seqlen):
        for j in xrange(i + min_n, min(seqlen, i + max_n) + 1):
            yield seq[i:j]

index = defaultdict(list)

for word in words:
    for ngram in ngrams(word.text, 2):
        index[ngram].append(word)


def possible_parallel(word_a, word_b):
    if len(word_a) != len(word_b):
        pass



for word_a, word_b in combinations(words, 2):
    header(word_a, word_b)


def report():
    for word in words:
        print()
        header(word)
        for letter in word.letters:
            header(letter, char='-')
            for match in letter.matches:
                print(match.word)
