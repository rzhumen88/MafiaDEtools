import os
import struct

def bytesFromStr(s:str):
    byteorder = '0123456789ABCDEF'
    bytestr = b''
    for i in range(0, len(s), 2):
        byte = (byteorder.find(s[i]) << 4) + byteorder.find(s[i+1])
        bytestr += struct.pack('B', byte)
    return bytestr

def pckg_build(file, path):
    filelist = os.listdir(path)
    bytestream = b''
    offset = 16
    with open(file, 'wb') as arc:
        arc.write(b'PCKG')
        arc.write(struct.pack('<I', 2))
        arc.write(struct.pack('<I', len(filelist)))
        arc.write(b'\xFF'*4)
        offset += len(filelist) * 32
        for f in filelist:
            namestr = f.split('.')[0]
            name = bytesFromStr(namestr)[::-1]
            with open(path+'/'+f, 'rb') as f:
                f = f.read()
                h, w = struct.unpack('II', f[12:20])
                flen = len(f)
                bytestream += f
                arc.write(name)
                arc.write(struct.pack('<I', offset))
                offset += flen
                arc.write(b'\x00'*4)
                arc.write(struct.pack('<I', flen))
                arc.write(struct.pack('<I', flen))
                arc.write(struct.pack('<H', h))
                arc.write(struct.pack('<H', w))
                arc.write(b'\x00'*4)
                print(f'{namestr} imported!')
        arc.write(bytestream)
        print(f'{file} built!')

                
if __name__ == '__main__':
    user_input = ''
    while True:
        user_input = input('To build .pckg file enter [pckg] [file directory]')
        user_input = user_input.split(' ')
        if os.path.isdir(user_input[1]) and os.path.isfile(user_input[0]):
            pckg_build(user_input[0], user_input[1])
            input()
            break
