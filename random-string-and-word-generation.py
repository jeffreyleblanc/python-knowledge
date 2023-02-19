#! /usr/bin/python3

'''
Shows basic ways of making random string, words, and numbers
'''

import random
import string
import subprocess


def random_lower(n=6):
    return ''.join(random.choices(string.ascii_lowercase,k=n))

def random_upper(n=6):
    return ''.join(random.choices(string.ascii_uppercase,k=n))

def random_digits(n=6):
    return ''.join(random.choices(string.digits,k=n))

def random_items(lst, n=None, min=None, max=None):
    # Will only choose a given items from lst once
    if n is not None:
        if n == 1:
            return random.sample(lst,k=2)[0]
        else:
            return random.sample(lst,k=n)
    else:
        return random.sample(lst,k=random.randint(min,max))

def random_words(n=10, dictionary='/usr/share/dict/american-english'):
    r = subprocess.run(['shuf',f'-n{n}',dictionary],stdout=subprocess.PIPE,text=True)
    return [e.replace("'s",'') for e in r.stdout.splitlines()]

def sort_words(word_list):
    names = []
    words = []
    for w in word_list:
        if w[0].isupper():
            names.append(w)
        else:
            words.append(w)
    return names,words

class WordSet:

    def __init__(self, n=1000):
        names,words = sort_words(random_words(n))
        self.names = names
        self.words = words

    def word(self):
        return self.words.pop()

    def name(self):
        return self.names.pop()

    def fullname(self):
        return f'{self.name()} {self.name()}'

    def title(self):
        return f"{self.name()}'s {self.word()} {self.word()}"

    def url(self):
        return f"https://{self.word()}.com"


if __name__ == '__main__':

    from os import get_terminal_size
    s = get_terminal_size()
    NCOLS = s.columns

    def R():
        print(f"\n{'-'*NCOLS}\n")
    def H(text):
        print(f"\n{'-'*NCOLS}\n{text}\n{'-'*NCOLS}\n")


    ws = WordSet()

    H('Random word and name')
    print(ws.word())
    print(ws.name())

    H('All random words')
    print(random_words())

    H('Sorted random words')
    names,words = sort_words(random_words(100))
    print(names)
    print(words)

    H('Sorted random lower strings')
    for i in range(4):
        print(random_lower())

    H('Sorted random upper strings')
    for i in range(4):
        print(random_upper())

    H('Sorted random digits')
    for i in range(4):
        print(random_digits())

    H('Sorted random key')
    for i in range(4):
        print(f"{random_lower(4)}-name")

    H('Random ints between 0 and 1')
    for i in range(4):
        print(random.randint(0,1))

    H('Random ints between 0 and 10')
    for i in range(4):
        print(random.randint(0,10))

    lst = list(range(20))
    H('Random choice sets fixed size')
    print(random.choices(lst,k=4))

    H('Random choice set random size')
    for i in range(3):
        print(random.choices(lst,k=random.randint(0,5)))
        R()

