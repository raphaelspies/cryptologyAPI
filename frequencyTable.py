from LETTERS import LETTERS
from englishFreqTable import englishFreqTable

def frequencyTable(ciphertext):
	table = {}
	for i in ciphertext:
		if i not in table:
			table[i] = 1
		else:
			table[i] += 1
	# return a dictionary of the table sorted in descending order
	table = dict(sorted(table.items(), key=lambda item: item[1], reverse = True))
	print (table)
	return table

def analyzeTable(freqTable):
	orderedEnglishTable = dict(sorted(englishFreqTable.items(), key=lambda item: item[1], reverse = True))
	EnglishKeys = list(orderedEnglishTable.keys())
	inputKeys = list(freqTable.keys())
	key = {}
	i = 0
	j = 0
	# for i in range (0, min(len(inputKeys), len(LETTERS))):
	while i < min(len(inputKeys), len(LETTERS)):
		currentLetter = inputKeys[i].lower()
		if (LETTERS.find(currentLetter) != -1):
			englishLetter = EnglishKeys[i]
			key[currentLetter] = englishLetter
			i += 1
			j += 1
		else:
			key[currentLetter] = inputKeys[i]
			i += 1
	return key

def makeEnglishFreqTable():
	return dict(sorted(englishFreqTable.items(), key=lambda item: item[1], reverse = True))

def assignPercent():
	denominator = len(FreqTable)
	numerator = 0
	for i in freqTable:
		numerator += freqTable[i]
	percentValue =  denominator/numerator

