'''
How to use:
    Run the code with the arguments encrypt, decrypt, brute_force, probability_crack or dictionary_crack, this will alter the text file and do what you request.
    To put or remove text just alter the contents of the text file
'''

import sys

# Does the CaesarCipher encryption
def encrypt(text, key):
    data = ""
    for letter in text:
        data = data + (chr((ord(letter) + key) % 256))
    return data

# Decrypts the code in case you already know the key
def decrypt(text, key):
    data = ""
    for letter in text:
        char = chr((ord(letter) - key) % 256)
        data = data + char
    return data

# Displays all possibilities for the user to choose the correct one
def bruteForce(text):

    # Runs all possible combination for the user to identify which one is text
    for potential_key in range(256):
        print("\nKey as ->", potential_key, ":")
        for i in range(len(text)):
            print(chr((ord(text[i]) + potential_key) % 256), end = "")
    
    key = int(input("\n\n\nChoose the key number that translated the text: "))

    # Returns the correct text so the file can be updated
    correct = ""
    for letter in text:
        correct = correct + chr((ord(letter) + key) % 256)

    return correct

# Tries to crack the code on the basis that the most used character is whitespace
def probabilityCrack(text):
    # Whitespaces are the most common characters in the english alphabet so you can guess that it will be within the top 3 most common characters in the text

    # Make a index of how much each letter appears in the text
    letter_occurance = [0] * 256

    for letter in text:
        letter_occurance[ord(letter)] += 1
    
    # Find the 3 most common characters
    third = first = second = -1
    keys = [0] * 3

    for i in range(len(letter_occurance)):
        if letter_occurance[i] > first:
            third = second
            keys[2] = keys[1]

            second = first
            keys[1] = keys[0]

            first = letter_occurance[i]
            keys[0] = i

        elif letter_occurance[i] > second:
            third = second
            keys[2] = keys[1]

            second = letter_occurance[i]
            keys[1] = i
 
        elif letter_occurance[i] > third:
            third = letter_occurance[i]
            keys[2] = i

    # Define their code - 32 (space) as the key.
    for i in range(len(keys)):
        keys[i] -= 32

    #solve for the 3 possible displayed keys
    possibilities = [""] * len(keys)
    for i in range(len(possibilities)):
        for letter in text:
            char = chr((ord(letter) - keys[i]) % 256)
            possibilities[i] = possibilities[i] + char
    
    # Show each text to the user for him to select the correct one
    for i in range(len(possibilities)): 
        print("Key", i, "reads as:", possibilities[i], "\n\n")

    correct = int(input("Which key is correct? "))

    return possibilities[correct]

# Tries to solve by analyzing if the words are in a dictionary. The one with the most matches will be the text (only works in the language of the dictionary)
def dictionaryCrack(text):
    
    # Opens the dictionary and takes the string
    dictionary_file = open("../dictionary.txt", "r")
    dictionary = dictionary_file.read()

    correct_words = [0] * 256
    for i in range(256):
        # In this all possible combinations of text_string will be tested
        test_string = "" 
        for letter in text:
            char = chr((ord(letter) + i) % 256)
            test_string = test_string + char

        test_string = test_string.split()
        
        for j in (test_string): 
            if j in dictionary: 
                correct_words[i] += 1

    dictionary_file.close()

    # Does the final encryption with the correct code
    key = 0
    for i in range(len(correct_words)): 
        if correct_words[key] < correct_words[i]: 
            key = i

    return decrypt(text, -key)

def main():

    key = 40

    text = open("CaesarCipher.txt", "r+")

    # Call the desired function or dont alter the text
    if sys.argv[1] == "encrypt":
        data = encrypt(text.read(), key)
    elif sys.argv[1] == "decrypt":
        data = decrypt(text.read(), key)
    elif sys.argv[1] == "brute_force":
        data = bruteForce(text.read())
    elif sys.argv[1] == "probability_crack":
        data = probabilityCrack(text.read())
    elif sys.argv[1] == "dictionary_crack":
        data = dictionaryCrack(text.read())
    else: 
        data = text.read()

    text.truncate(0)
    text.seek(0)
    text.write(data)
    text.close()

if __name__ == "__main__":
    main()