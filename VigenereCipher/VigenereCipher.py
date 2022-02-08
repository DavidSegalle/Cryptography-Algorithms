from __future__ import unicode_literals
from enum import unique
import sys
from suffix_trees import STree
import kasiski
from os import path

'''
How to use:
    pip install suffix-tree
        DON'T RUN "PIP INSTALL" AS AN ADMIN
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

    text = open(path.join(path.dirname(__file__), "VigenereCipher.txt"), "r+")

    keyword = "caca"

    data = text.read()

    if sys.argv[1] == "encrypt":
        data = encrypt(data, keyword)
    elif sys.argv[1] == "decrypt":
        data = decrypt(data, keyword)
    elif sys.argv[1] == "kasiski":
        data = kasiski.kasiski(data, 8)

    text.truncate(0)
    text.seek(0)
    text.write(data)
    text.close()

if __name__ == "__main__": 
    main()
