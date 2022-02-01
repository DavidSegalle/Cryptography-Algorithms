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
    
    return distances

def kasiski(text):
    stree = STree.STree(text)

    repeated_substrings_set = findSubstring(stree, text)

    repeated_substrings = setToArray(repeated_substrings_set)

    distances = calcDistances(repeated_substrings)

    print(distances)

    # The largest common factor of all the distances is the key length

    # Use CaesarCipher probability crack for each sequence of letters in the text. A match is when one of the 3 most common characters in english are also the most common in the text

    # Show the user all matches combinations so he can choose the correct one or use a dictionary
    return text