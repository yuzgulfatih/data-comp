import zlib

def deflate_compress(input_file, output_file):
    with open(input_file, 'rb') as file_in:
        with open(output_file, 'wb') as file_out:
            compressobj = zlib.compressobj()
            for chunk in iter(lambda: file_in.read(1024), b''):
                compressed_chunk = compressobj.compress(chunk)
                file_out.write(compressed_chunk)
            compressed_tail = compressobj.flush()
            file_out.write(compressed_tail)

# Kullanım örneği
input_file = 'deflate\data.txt'
output_file = 'deflate\data_compressed.deflate'
deflate_compress(input_file, output_file)
