from LETTERS import LETTERS

# create the cipher table
def createColumnarTable(key):
	key = key.lower()
# 1. take key and remove all duplicates and spaces
	key = key.replace(" ", "")
	# keyset = set(key)
	keyset = {}
	for h in key:
		if h not in keyset:
			keyset[h] = 1
# 2. Create a string for each "column", then push one letter from key onto it
	listkey = list(keyset)
	currentCol = 0
# 3. Iterate over remainder of alphabet, adding a letter to each column
	i = 0
	while (i < len(LETTERS)):
		# skip any letter that is already in the key
		if(key.find(LETTERS[i]) != -1):
			i += 1
		else:
			listkey[currentCol] += LETTERS[i]
			currentCol = (currentCol + 1) % len(listkey)
			i += 1
# create the key from the cipher table
# 1. concatenate all the columns together
	ciphertable = ""
	for j in listkey:
		ciphertable += j
	print("ciphertable: ", ciphertable)
	return ciphertable
