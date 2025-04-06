import os
import struct

def byteStreamToStr(bs: bytes):
    s = ''
    for b in bs:
        s += hex(b)[2:].zfill(2)
    return s.upper()

def pckgExtract(filename: str):
    dir_name = filename.replace('.pckg', '')
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    with open(filename, 'rb') as f:
        data = f.read(16)
        header = data[:4]
        ver, total_files = struct.unpack('II', data[4:12])
        file_info_size = total_files * 32
        if not header == b'PCKG':
            print('Wrong header')
            return 0
        data = f.read(file_info_size)
        for i in range(0, file_info_size, 32):
            name = byteStreamToStr(data[i:i+8][::-1])
            offset, _, size, _, height, width, _ = struct.unpack('IIIIHHI', data[i+8:i+32])
            f.seek(offset)
            extracted = f.read(size)
            extracted_name = dir_name+'/'+name+'.dds'
            with open(extracted_name, 'wb') as f2:
                f2.write(extracted)
                print(f'Extracted: {extracted_name} | {width}x{height} | Size: {round(size/1000, 2)}kb')

if __name__ == '__main__':
    user_input = ''
    while not os.path.isfile(user_input):
        user_input = input('Path to .pckg file: ')
    pckgExtract(user_input)
    input('done!')
