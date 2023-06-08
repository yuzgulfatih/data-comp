import zlib

def deflate_decompress(input_file, output_file):
    with open(input_file, 'rb') as file_in:
        with open(output_file, 'wb') as file_out:
            decompressobj = zlib.decompressobj()
            for chunk in iter(lambda: file_in.read(1024), b''):
                decompressed_chunk = decompressobj.decompress(chunk)
                file_out.write(decompressed_chunk)
            decompressed_tail = decompressobj.flush()
            file_out.write(decompressed_tail)

# Kullanım örneği
input_file = 'deflate\data_compressed.deflate'
output_file = 'deflate\data_decompressed.txt'
deflate_decompress(input_file, output_file)
