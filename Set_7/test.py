import random
import re
import string
import time

LENGTH = 10
LIST_SIZE = 1000000

def generate_word():
    word = [random.choice(string.ascii_lowercase) for _ in range(LENGTH)]
    word = ''.join(word)
    return word

wordlist = [generate_word() for _ in range(LIST_SIZE)]

start = time.time()
[re.search('python', word) for word in wordlist]
print('search:', time.time() - start)

start = time.time()
[re.match('(.*?)python(.*?)', word) for word in wordlist]
print('match:', time.time() - start)