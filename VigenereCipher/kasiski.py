#from numpy import common_type
from suffix_trees import STree

#from VigenereCipher.VigenereCipher import decrypt


'''
    This are the most common characters in english text, if your text isn't being decyphered try adding more letters from most common to least, doing that will impact speeds
'''
common_letter = " eta"




# Finds all substrings of size > 3 present in the ciphertext and returns them as a sorted array
def findSubstring(stree, text):
    repeated_substrings_set = []

    for substring_length in range(3, int(len(text) / 2)):
        for substring in range(0, len(text) - substring_length):
            if 3 <= len(stree.find_all(text[substring : substring + substring_length])):
                repeated_substrings_set.append(stree.find_all(text[substring : substring + substring_length]))

    return repeated_substrings_set




# Turns the set of substrings into an array to make it easier to work with
def setToArray(repeated_substrings_set):
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

    return unique_substrings




# Calculates the distance between the positions of equal substrings in the array
def calcDistances(repeated_substrings):
    distances = []

    for substring in repeated_substrings:
        for j in range(len(substring) - 1):
            distances.append(substring[j + 1] - substring[j])
    
    distances.sort(reverse = True)
    return distances




def highestCommonFactor(values):

    # Find the factors of each number in values
    factors = []
    for i in values:
        factors.append(i)
        for j in range(1, (i // 2) + 1, 1):
            if not (i % j):
                factors.append(j)

    factors.sort()

    return factors




def findKeys(text):    
    
    # Count how many of each character
    common_text = [0] * 255
    for letter in text:
        common_text[ord(letter)] += 1
    
    # The largest number in common_text is one of the characters
    largest_pos = 0
    for i in range(len(common_text)):
        if common_text[i] >= common_text[largest_pos]:
            largest_pos = i

    # The keys for that bit of text could be:
    keys = []
    for i in common_letter:
        keys.append(largest_pos - ord(i))
    
    return keys




def dictionaryTest(text):
    dictionary_file = open("../dictionary.txt", "r")
    dictionary = dictionary_file.read()

    words = text.split()

    correct_words = 0
    for word in (words): 
            if word in dictionary: 
                correct_words += 1
    
    if correct_words > len(words) / 2:
        return text
    return None




def getCorrectText(text, keys):

    index_manager = [0] * len(keys)

    for i in range(len(keys[0]) ** len(keys)):#range(len(keys) * len(keys[0])):

        index_manager[-1] += 1

        for j in range(len(index_manager) - 1, -1, -1):

            if index_manager[j] >= len(keys[0]):# and j > 0:
                index_manager[j] = 0
                index_manager[j - 1] += 1

        keyword = ""
        for j in range(len(keys)):

            aux = keys[j][index_manager[j]]
            keyword += chr(aux)
        
        # Attempt dictionaryCrack on the keyword




def probableKeys(text, length):
    
    # Use the length to assume which letter of the ciphertext was used
    divided_text = [""] * length
    i = 0
    while i < length:
        position = i
        while position < len(text):
            a = text[position]
            divided_text[i] += a
            position += length
        i += 1
    
    # Use probability for each member of divided_text to get the 4 most likely keys
    # Will use a different form of probability to what is used in CaesarCipher
    keys = []
    for i in divided_text:
        keys.append(findKeys(i))

    return keys




def likelyKeysCombo(text, key_lengths):

    # Start by the largest keys since they are the most likely ones
    keys = []

    for i in range(len(key_lengths) - 1, -1, -1):
        # For each key length use probability crack to figure out which are the most likey keys
        keys.append(probableKeys(text, key_lengths[i]))
    return keys




# Attempts to break VigenereCipher using kasiski algorithm and some probability
def kasiski(text, max_key_size):
    stree = STree.STree(text)

    repeated_substrings_set = findSubstring(stree, text)

    repeated_substrings = setToArray(repeated_substrings_set)

    distances = calcDistances(repeated_substrings)

    # The correct key is most likely the biggest one (given a limit to not test ridiculously large keys)
    all_key_lengths = highestCommonFactor(distances)

    key_lengths = []
    # Will only test keys of size > 3 and smaller than what you decide as max
    for i in all_key_lengths:
        if i < max_key_size and i >= 3 and not(i in key_lengths):
            key_lengths.append(i)

    keys = likelyKeysCombo(text, key_lengths)
    
    # keys[0] deve ser modificado pra pegar todos os tamanhos de chave possíveis
    getCorrectText(text, keys[0])

    # Use probability crack to see the most likely keys for each letter and test them against each other using a dictionary

    # Use CaesarCipher probability crack for each sequence of letters in the text. A match is when one of the 3 most common characters in english are also the most common in the text

    # Show the user all matches combinations so he can choose the correct one or use a dictionary
    return text