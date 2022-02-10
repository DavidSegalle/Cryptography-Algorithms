import sys
import random

def saveToFile(data, file):
    file.truncate(0)
    file.seek(0)
    file.write(data)

def encrypt(data_file, key_file):

    data = data_file.read()

    key = ""

    # String of pseudo random asc2 characters of the same size as the text  
    for i in data:
        key += chr(random.randint(0, 256))

    # Encrypts the file using the XOR operator
    # The XOR operator is reversible so to find the text just run the same algorithm with the ciphertext and the same key
    encrypted = ""
    for i in range(len(data)):
        encrypted += chr(ord(data[i]) ^ ord(key[i]))

    saveToFile(encrypted, data_file)
    # The key is saved so you can dexrypt the data, if the text is encrypted twice and a key is not saved the data is lost forever
    saveToFile(key, key_file)

def decrypt(data_file, key_file):

    ciphertext = data_file.read()
    key = key_file.read()

    # Decrypts the data using the key in Keyword.txt and the XOR operator
    data = ""
    for i in range(len(ciphertext)):
        data += chr(ord(ciphertext[i]) ^ ord(key[i]))

    saveToFile(data, data_file)
    


def main():

    data_file = open("OneTimePad.txt", "r+")
    key_file = open("Keyword.txt", "r+")
	
    if len(sys.argv) < 2:
        print("Missing arguments")
    elif sys.argv[1] == "encrypt":
        encrypt(data_file, key_file)
    elif sys.argv[1] == "decrypt":
        decrypt(data_file, key_file)

    data_file.close()
    key_file.close()

if __name__ == "__main__":
	main()