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

    Run the program with the argument encrypt to encrypt it and decrypt to decrypt with the key you already have. If you don't know the key run the argument kasiski it will try to break the encryption using kasiski algorithm.

    The encryption and decryption key can be found in the main function, for time constraint reasons the algorithm will only break keys of up to 8 characters, if you want more you can increase it, however, it may take longer to run

    The kasiski algorithm, while not instant can turn 10 hours of waiting into a few seconds.
'''

# encripts file with the VigenereCipherAlgorithm
def encrypt(text, keyword):
    
    encrypted = ""

    encrypted = ""
    for i in range(len(text)):
        encrypted += chr((ord(text[i]) + ord(keyword[i % len(keyword)])) % 256)

    return encrypted

# decripts file with the VigenereCipherAlgorithm (key is necessary)
def decrypt(text, keyword):

    decrypted = ""

    decrypted = ""
    for i in range(len(text)):
        decrypted += chr((ord(text[i]) - ord(keyword[i % len(keyword)])) % 256)

    return decrypted

# Sets the function calls for what the user wants to do.
def main(): 

    text = open(path.join(path.dirname(__file__), "VigenereCipher.txt"), "r+")

    keyword = "keyword"

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
