import sys

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
def kasiski(text):
    # Find repeated substrings of at least 3 characters in the ciphertext (initial problem)

    # For every repeated substring, figure out their distances and the factors that make them up (if distance is 30 the factors are 2 * 3 * 5)

    # The largest common factor of all the distances is the key length

    # Use CaesarCipher probability crack for each sequence of letters in the text. A match is when one of the 3 most common characters in english are also the most common in the text

    # Show the user all matches combinations so he can choose the correct one or use a dictionary
    pass

# Sets the function calls for what the user wants to do.
def main(): 

    text = open("VigenereCipher.txt", "r+")

    keyword = "palavra"

    data = text.read()

    if sys.argv[1] == "encrypt":
        data = encrypt(data, keyword)
    if sys.argv[1] == "decrypt":
        data = decrypt(data, keyword)
    if sys.argv[1] == "kasiski":
        data = kasiski(data)

    text.truncate(0)
    text.seek(0)
    text.write(data)
    text.close()

if __name__ == "__main__": 
    main()