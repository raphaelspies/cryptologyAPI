import random
from LETTERS import LETTERS

def createRandomTable(letters):
	table = ''
	lettersleft = letters.lower()
	for i in letters:
		#get a random letter from remaining letters
		s = random.randint(0, len(lettersleft) - 1)
		k = lettersleft[s]
		#add that letter to table
		table = table + k
		#remove that letter from lettersleft
		lettersleft = lettersleft.replace(k, '')
		# print(lettersleft) <-- will verify that each letter is only used once
	print(table)
	return table

def encode(plaintext, key):
	encoded = ''
	for i in plaintext:
		#check if the current letter would have been added to encryption key
		#by checking if it's in LETTERS
		if (LETTERS.find(i) != -1):
			#get a numeric value for i's plaintext character
			transposeCount = LETTERS.index(i)
			#get the corresponding encrypted character
			transposedVal = key[transposeCount]
			encoded = encoded + transposedVal
	return encoded

def decode(ciphertext, key):
	decoded = ''
	for i in ciphertext:
		# if letter exists in original range
		if (LETTERS.find(i) != -1):
			# find that letter's index in the key
			transposeCount = key.index(i)

			transposedVal = LETTERS[transposeCount]
			decoded = decoded + transposedVal
	return decoded