from numpy import common_type
from suffix_trees import STree

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

    # Most common characters are ' ', 'e', 't' so assume that one of them is the most common in the text

    common_letter = " et"
    common_text = [0] * 255
    for letter in text:
        common_text[ord(letter)] += 1


def probableKeys(text, length):
    
    # Use the length to assume which letter of the ciphertext was used
    iterations = len(text) // length
    print(length)
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
    for i in divided_text:
        findKeys(i)

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

    likelyKeysCombo(text, key_lengths)

    # Use probability crack to see the most likely keys for each letter and test them against each other using a dictionary

    # Use CaesarCipher probability crack for each sequence of letters in the text. A match is when one of the 3 most common characters in english are also the most common in the text

    # Show the user all matches combinations so he can choose the correct one or use a dictionary
    return text