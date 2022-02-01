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

# Attempts to crack the encription by using kasiski's algorithm
'''def kasiski(text):
    # Find repeated substrings of at least 3 characters in the ciphertext (initial problem)
    stree = STree.STree(text)

    repeated_substrings_set = []

    # Finds all substrings of size > 3 present in the ciphertext
    for substring_length in range(3, int(len(text) / 2)):
        for substring in range(0, len(text) - substring_length):
            if 3 <= len(stree.find_all(text[substring : substring + substring_length])):
                repeated_substrings_set.append(stree.find_all(text[substring : substring + substring_length]))

    # Makes all the sets into arrays and sorts them (sets can't be sorted or use the [] operator)
    repeated_substrings = []
    for i in range(len(repeated_substrings_set)):
        aux = []
        for j in range(len(repeated_substrings_set[i])):
            aux.append(repeated_substrings_set[i].pop())

        repeated_substrings.append(aux)

    for i in repeated_substrings:
        i.sort()
    repeated_substrings.sort()

    # Delete obviously equal substrings
    unique_substrings = []
    for i in repeated_substrings:
        if not(i in unique_substrings):
            unique_substrings.append(i)

    del repeated_substrings_set
    del repeated_substrings

    # Distance for each substring
    distances = []

    for substring in unique_substrings:
        for j in range(len(substring) - 1):
            distances.append(substring[j + 1] - substring[j])

    # distances.sort() Might not be necessary
    print(distances)

    # The largest common factor of all the distances is the key length

    # Use CaesarCipher probability crack for each sequence of letters in the text. A match is when one of the 3 most common characters in english are also the most common in the text

    # Show the user all matches combinations so he can choose the correct one or use a dictionary
    return text'''

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
        data = kasiski.kasiski(data)

    text.truncate(0)
    text.seek(0)
    text.write(data)
    text.close()

if __name__ == "__main__": 
    main()
