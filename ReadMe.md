# Cryptology API

## Routes:
### 1. POST /randomSubstitution
#### REQUEST:
| key | value |
|-----|-------|
| key | *optional* If you have an encryption key (a 26-letter randomized alphabet), use it to encrypt |
| plaintext | A string of text you would like to encrpyt |

##### RESPONSE:
| key | value |
|-----|-------|
| key | the 26-letter randomized alphabet that was used to encrypt |
| ciphertext | the encrypted response |
<br/>

### 2. POST /columnarSubstitution
#### REQUEST:
| key | value |
|-----|-------|
| key | A phrase or group of letters that will be used to create a columnar substitution table |
| plaintext | A string of text you would like to encrpyt |

#### RESPONSE:
| key | value |
|-----|-------|
| key | the 26-letter columnar substitution table that was used to encrypt |
| ciphertext | the encrypted response |
<br/>

### 3. POST /decrypt
#### REQUEST:
| key | value |
|-----|-------|
| key | the 26-letter substitution cipher key that was used to encrypt |
| ciphertext | the encrypted text you would like to decrypt |

#### RESPONSE:
| key | value |
|-----|-------|
| key | the 26-letter substitution cipher key that was used to encrypt |
| ciphertext | the decrypted plaintext message (all lowercase and without spacing or punctuation) |