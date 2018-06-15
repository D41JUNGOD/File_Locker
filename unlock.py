from Crypto.Cipher import AES

import os,struct,hashlib

def unlock_file(key, in_filename, chunksize=24*1024):
    key = hashlib.sha256(key).digest()
    out_filename = os.path.splitext(in_filename)[0]
    with open(in_filename, 'rb') as infile:
        password = infile.read(32)
        if not password == key:
            return 0
        origsize = struct.unpack('<Q',infile.read(struct.calcsize('Q')))
        iv = infile.read(16)
        mode = AES.MODE_CBC                                     #AES CBC모드 설정
        decryptor = AES.new(key,mode,iv)

        with open(out_filename,'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(origsize[0])

    os.unlink(in_filename)