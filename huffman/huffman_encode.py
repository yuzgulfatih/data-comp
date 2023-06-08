import heapq
import os
import pickle

class HuffmanNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def calculate_frequencies(text):
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


def build_huffman_tree(frequencies):
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


def generate_codes(node, current_code, codes):
    if node is None:
        return
    if node.character is not None:
        codes[node.character] = current_code
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)


def compress_text(text):
    frequencies = calculate_frequencies(text)
    huffman_tree = build_huffman_tree(frequencies)
    codes = {}
    generate_codes(huffman_tree, "", codes)
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    padding_amount = 8 - len(encoded_text) % 8  # Add padding to make the length a multiple of 8
    encoded_text += "0" * padding_amount
    padded_info = "{0:08b}".format(padding_amount)
    encoded_text = padded_info + encoded_text
    byte_array = bytearray()
    for i in range(0, len(encoded_text), 8):
        byte = encoded_text[i:i + 8]
        byte_array.append(int(byte, 2))
    return byte_array, huffman_tree


def write_compressed_file(file_path, compressed_data):
    file_name, file_ext = os.path.splitext(file_path)
    compressed_file_path = file_name + "_compressed" + file_ext
    with open(compressed_file_path, 'wb') as file:
        file.write(compressed_data)


def compress_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    compressed_data, huffman_tree = compress_text(text)
    write_compressed_file(file_path, compressed_data)
    return huffman_tree

def save_huffman_tree(huffman_tree, output_file_path):
    with open(output_file_path, 'wb') as file:
        pickle.dump(huffman_tree, file)



# Örnek kullanım:
file_path = 'data.txt'
huffman_tree = compress_file(file_path)
huffman_tree_file_path = 'huffman_tree.pkl'
save_huffman_tree(huffman_tree, huffman_tree_file_path)
print("Dosya sıkıştırıldı. Huffman ağacı oluşturuldu.")