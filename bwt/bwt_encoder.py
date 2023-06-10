import bz2

def bwt_compress_file(input_file, output_file):
    # Dosyanın içeriğini metin olarak oku
    with open(input_file, 'r') as file:
        input_text = file.read()

    # BWT sıkıştırma işlemi
    compressed_text = bz2.compress(input_text.encode())

    # Sıkıştırılmış metni dosyaya yaz
    with open(output_file, 'wb') as file:
        file.write(compressed_text)

# Kullanım örneği
input_file = 'bwt\data.txt'
output_file = 'bwt\compressed.bwt'
bwt_compress_file(input_file, output_file)

