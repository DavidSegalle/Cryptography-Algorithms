from __future__ import unicode_literals
from enum import unique
import sys
from suffix_trees import STree
import kasiski

'''
How to use:
    pip install suffix-tree
'''

# encripts file with the VigenereCipherAlgorithm
def encrypt(text, keyword):
    
    over = False
    word_index = 0
    encrypted = ""

    while(not over):
        if word_index >= len(text) - 1:
            over = True

        letter = chr(ord(text[word_index]) + ord(keyword[word_index % len(keyword)]) % 256)
        encrypted = encrypted + letter
        word_index += 1
        
    return encrypted

# decripts file with the VigenereCipherAlgorithm (key is necessary)
def decrypt(text, keyword):

    over = False
    word_index = 0
    decrypted = ""

    while(not over):
        if word_index >= len(text) - 1:
            over = True

        letter = chr(ord(text[word_index]) - ord(keyword[word_index % len(keyword)]) % 256)
        decrypted = decrypted + letter
        word_index += 1
        
    return decrypted

# Sets the function calls for what the user wants to do.
def main(): 

    text = open("VigenereCipher.txt", "r+")

    keyword = "chave"

    data = text.read()

    if sys.argv[1] == "encrypt":
        data = encrypt(data, keyword)
    if sys.argv[1] == "decrypt":
        data = decrypt(data, keyword)
    if sys.argv[1] == "kasiski":
        data = kasiski.kasiski(data, 16)

    text.truncate(0)
    text.seek(0)
    text.write(data)
    text.close()

if __name__ == "__main__": 
    main()
