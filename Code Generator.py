def encode_word(word):
    """
    Encode a word into numbers based on a predefined mapping.
    """
    encoding = {
        'a': '126', 'b': '225', 'c': '324', 'd': '423', 'e': '522',
        'f': '621', 'g': '720', 'h': '819', 'i': '918', 'j': '1017',
        'k': '1116', 'l': '1215', 'm': '1314', 'n': '1413', 'o': '1512',
        'p': '1611', 'q': '1710', 'r': '1809', 's': '1908', 't': '2007',
        'u': '2106', 'v': '2205', 'w': '2304', 'x': '2403', 'y': '2502', 'z': '2601'
    }

    encoded_word = ""
    for char in word:
        if char.lower() in encoding:
            encoded_word += encoding[char.lower()] + " "
        else:
            encoded_word += char + " "
    return encoded_word.strip()


def main():
    while True:
        word = input("Please enter word(s) to encrypt (or type 'terminate' to exit): ")
        if word.lower() == 'terminate':
            print("Exiting the program...")
            break
        else:
            encoded_word = encode_word(word)
            print("Encoded word:", encoded_word)


if __name__ == "__main__":
    main()

#the code is a letter to number map sequentially ordered then added at the end to the order in reverse
#this mapping links each letter to its' place from 1-26 and 26-1