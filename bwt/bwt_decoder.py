import bz2

def bwt_decompress_file(input_file, output_file):
    # Sıkıştırılmış dosyanın içeriğini oku
    with open(input_file, 'rb') as file:
        compressed_data = file.read()

    # Sıkıştırılmış veriyi BWT ile çöz
    decompressed_data = bz2.decompress(compressed_data).decode()

    # Çözülmüş veriyi dosyaya yaz
    with open(output_file, 'w') as file:
        file.write(decompressed_data)

# Kullanım örneği
input_file = 'bwt\compressed.bwt'
output_file = 'bwt\decompressed.txt'
bwt_decompress_file(input_file, output_file)
