echo "import itertools
from mnemonic import Mnemonic
import time

mnemo = Mnemonic('english')

words_filename = input('Input filename of words to use to permutate : ')
validseeds_filename = input('Input name of filename to save valid seeds  : ')

words = open(words_filename, 'r')
validseeds = open(validseeds_filename, 'w')

st = time.time()

def produce_partially_set(wordlist):
    wordlist.insert(0, 'dutch')
    wordlist.insert(4, 'fog')
    wordlist.append('parrot')
    return wordlist

for index, line in enumerate(words):
	line = line.split()
	perms = itertools.permutations(line, 9)
	for i in perms:
		mystring = ' '.join(i)
		splitstrings = mystring.split()
		perms = produce_partially_set(splitstrings)
		seed = ' '.join(perms)
		isValid = mnemo.check(seed)
		if isValid:
			validseeds.write(f'{seed}'+'\n')
		else:
			pass
print('total permutations : ', index, end='\r')
elapsed_time = time.time() - st
print('Execution time:', time.strftime('%H:%M:%S', time.gmtime(elapsed_time)))" > x.py