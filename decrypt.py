from LETTERS import LETTERS

def decrypt(ciphertext, cipher):
	decoded = ''
	ciphertext = ciphertext.lower()
	for k in ciphertext:
		# if letter exists in original range
		if (LETTERS.find(k) > -1):
			# find that letter's index in the key
			transposeCount = cipher.index(k)

			transposedVal = LETTERS[transposeCount]
			decoded = decoded + transposedVal
	print(decoded)
	return decoded