import heapq
import pickle
import os


class HuffmanNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def rebuild_huffman_tree(frequencies):
    priority_queue = [[weight, HuffmanNode(key, weight)] for key, weight in frequencies.items()]
    heapq.heapify(priority_queue)
    while len(priority_queue) > 1:
        lo = heapq.heappop(priority_queue)
        hi = heapq.heappop(priority_queue)
        merged_node = HuffmanNode(None, lo[0] + hi[0])
        merged_node.left = lo[1]
        merged_node.right = hi[1]
        heapq.heappush(priority_queue, [merged_node.frequency, merged_node])
    return priority_queue[0][1]


def decompress_text(compressed_data, huffman_tree):
    encoded_text = ''.join(format(byte, '08b') for byte in compressed_data)

    padding_amount = int(encoded_text[:8], 2)
    encoded_text = encoded_text[8:-padding_amount]

    current_node = huffman_tree
    decompressed_text = ""
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.character:
            decompressed_text += current_node.character
            current_node = huffman_tree

    return decompressed_text


def decompress_file(compressed_file_path, huffman_tree_path):
    with open(compressed_file_path, 'rb') as file:
        compressed_data = file.read()

    with open(huffman_tree_path, 'rb') as file:
        huffman_tree = pickle.load(file)

    decompressed_text = decompress_text(compressed_data, huffman_tree)

    return decompressed_text


# Örnek kullanım:
compressed_file_path = 'data_compressed.txt'
huffman_tree_path = 'huffman_tree.pkl'

decompressed_text = decompress_file(compressed_file_path, huffman_tree_path)
print("Dosya geri dönüştürüldü.")
print("Geri Dönüştürülen Metin: ", decompressed_text)
