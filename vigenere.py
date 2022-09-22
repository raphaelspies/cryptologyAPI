from LETTERS import LETTERS
import random

def createTable(length, startingKey):
    fullAlphabets = length / 26
    addLetters = length % 26
    subtractLetters = startingKey
    table = LETTERS[subtractLetters:]
    for a in range(0, fullAlphabets + 1):
      table += LETTERS
    table += LETTERS[0:(subtractLetters + addLetters)]
    return table

def vigenere(plaintext):
  plaintext = plaintext.lower()
  print(len(plaintext))

  subtractKey = random.randint(0, 25)
  cipherTable = createTable(len(plaintext), subtractKey)
  encoded = ''
  print(cipherTable)
  print(len(cipherTable))
  for i in range(0, len(plaintext)):
    currentLetter = plaintext[i]
    print(i, cipherTable[LETTERS.find(currentLetter) + i])
    if (LETTERS.find(currentLetter) != -1):
      cipherLetter = cipherTable[LETTERS.index(currentLetter) + i]
      encoded += cipherLetter
  return {encoded, subtractKey}

input = "abcdefghijklmnopqurstuvwxyzab"
output = vigenere(input)
print(output)