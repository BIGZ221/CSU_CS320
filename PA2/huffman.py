import sys
import heapq

def file_character_frequencies(file_name):
    freqs = {}
    with open(file_name) as f:
      contents = f.read()
      for c in contents:
        freqs[c] = freqs.get(c, 0) + 1
    return freqs

class PriorityTuple(tuple):
    """A specialization of tuple that compares only its first item when sorting.
    Create one using double parens e.g. PriorityTuple((x, (y, z))) """
    def __lt__(self, other):
        return self[0] < other[0]

    def __le__(self, other):
        return self[0] <= other[0]

    def __gt__(self, other):
        return self[0] > other[0]

    def __ge__(self, other):
        return self[0] >= other[0]

    def __eq__(self, other):
        return self[0] == other[0]

    def __ne__(self, other):
        x = self.__eq__(other)
        return not x

def buildHuffmanTree(huffmanHeap):
    huffmanTree = huffmanHeap
    while len(huffmanTree) > 1:
      min1 = heapq.heappop(huffmanTree)
      min2 = heapq.heappop(huffmanTree)
      sum = min1[0] + min2[0]
      heapq.heappush(huffmanTree, PriorityTuple((sum, (min2, min1))))
    return huffmanTree[0]

def buildHuffmanHeap(frequencies):
    huffmanHeap = []
    freqs = frequencies.items()
    for key, value in freqs:
      heapq.heappush(huffmanHeap, PriorityTuple((value, key)))
    return huffmanHeap

def getHuffmanCode(huffmanTree, code=""):
    huffmanCodes = {}
    freq = huffmanTree[0]
    left = huffmanTree[1][0]
    right = huffmanTree[1][1]
    if isinstance(left[1], str):
      huffmanCodes[left[1]] = code + "0"
    else:
      huffmanCodes.update(getHuffmanCode(left, code + "0"))
    if isinstance(right[1], str):
      huffmanCodes[right[1]] = code + "1"
    else:
      huffmanCodes.update(getHuffmanCode(right, code + "1"))
    return huffmanCodes


def huffman_codes_from_frequencies(frequencies):
    huffmanHeap = buildHuffmanHeap(frequencies)
    huffmanTree = buildHuffmanTree(huffmanHeap)
    huffmanCode = getHuffmanCode(huffmanTree)
    return huffmanCode

def huffman_letter_codes_from_file_contents(file_name):
    """WE WILL GRADE BASED ON THIS FUNCTION."""
    # Suggested strategy...
    freqs = file_character_frequencies(file_name)
    return huffman_codes_from_frequencies(freqs)

def encode_file_using_codes(file_name, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    file_name_encoded = file_name + "_encoded"
    with open(file_name_encoded, 'w') as fout:
        for c in contents:
            fout.write(letter_codes[c])
    print("Wrote encoded text to {}".format(file_name_encoded))

def decode_file_using_codes(file_name_encoded, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name_encoded) as f:
        contents = f.read()
    file_name_encoded_decoded = file_name_encoded + "_decoded"
    codes_to_letters = {v: k for k, v in letter_codes.items()}
    with open(file_name_encoded_decoded, 'w') as fout:
        num_decoded_chars = 0
        partial_code = ""
        while num_decoded_chars < len(contents):
            partial_code += contents[num_decoded_chars]
            num_decoded_chars += 1
            letter = codes_to_letters.get(partial_code)
            if letter:
                fout.write(letter)
                partial_code = ""
    print("Wrote decoded text to {}".format(file_name_encoded_decoded))

def main():
    """Provided to help you play with your code."""
    import pprint
    frequencies = file_character_frequencies(sys.argv[1])
    pprint.pprint(frequencies)
    codes = huffman_codes_from_frequencies(frequencies)
    encode_file_using_codes("example.txt", codes)
    decode_file_using_codes("example.txt_encoded", codes)
    pprint.pprint(codes)


if __name__ == '__main__':
    """We are NOT grading you based on main, this is for you to play with."""
    main()
