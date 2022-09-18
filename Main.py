from flask import Flask, redirect, url_for, request
app = Flask(__name__)

from encrypt import encrypt
from decrypt import decrypt
from LETTERS import LETTERS
from frequencyTable import frequencyTable, analyzeTable, makeEnglishFreqTable
from englishFreqTable import englishFreqTable
from columnarSubstitution import createColumnarTable
from randomSubstitution import createRandomTable

# @app.route('/success/<name>')
# def success(name):
#   return 'welcome %s' % name

# @app.route('/login', methods = ['POST', 'GET'])
# def instructions():
#   if request.method == 'GET':
#     user = request.form['name']
#     return redirect(url_for('success', name = user))
#   else:
#     user = request.args.get('name')
#     return redirect(url_for('success', name = user))

@app.route('/')
def welcome():
  return 'Here is a list of all the routes we have:'

@app.route('/randomSubstitution', methods = ['POST'])
def encodeRandomSubstitution():
  plaintext = request.form['plaintext']
  if 'key' in request.form:
    randomTable = request.form['key']
  else:
    randomTable = createRandomTable(LETTERS)
  ciphertext = encrypt(plaintext, randomTable)
  return (f'key: {randomTable} \n ciphertext: {ciphertext}')

@app.route('/decode', methods = ['POST'])
def decodeRandomSubstitution():
  ciphertext = request.form['ciphertext']
  key = request.form['key']
  plaintext = decrypt(ciphertext, key)
  return (f'key: {key} \n plaintext: {plaintext}')

@app.route('/columnarSubstitution', methods = ['POST'])
def encodeColumnarSubstitution():
  plaintext = request.form['plaintext']
  if 'key' in request.form:
    inputKey = request.form['key']
    columnarTable = createColumnarTable(inputKey)
  ciphertext = encrypt(plaintext, columnarTable)
  return (f'key: {columnarTable} \n ciphertext: {ciphertext}')

if __name__ == '__main__':
  app.run(debug = True)