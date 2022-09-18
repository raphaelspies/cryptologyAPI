from LETTERS import LETTERS
# encrypt
# 1. same substitution cipher key
def encrypt(plaintext, key):
	encoded = ''
	plaintext = plaintext.lower()
	for j in plaintext:
		#check if the current letter would have been added to encryption key
		#by checking if it's in LETTERS
		if (LETTERS.find(j) != -1):
			#get a numeric value for i's plaintext character
			transposeCount = LETTERS.index(j)
			#get the corresponding encrypted character
			transposedVal = key[transposeCount]
			encoded = encoded + transposedVal
	print("plaintext: ", plaintext)
	print("encoded: ", encoded)
	return encoded