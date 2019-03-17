import sys
from itertools import islice


# Offset of alphabet in unicode
ORDER_OFFSET = 1072

# Height of character (in lines) in file
CHARACTER_HEIGHT = 8

# Number of lines in alphabet file
ALPHABET_HEIGHT = 8 * 33

inpt = sys.argv[1].lower()
alphabet = []

with open('alphabet.txt') as f:
    while True:
        ascii_char = list(islice(f, CHARACTER_HEIGHT)) 
        if ascii_char:                     
            alphabet.append(ascii_char)
        else:
            break

for phrase in inpt.split(' '):
	for counter in range(CHARACTER_HEIGHT):
		for char in phrase:
			index = ord(char) - ORDER_OFFSET
			if char == 'ё':
				index -= 1
			print(alphabet[index][counter][:-1], end=' ')
		print()
	print()
