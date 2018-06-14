from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

import os,struct,hashlib

def encrypt_file(key, in_filename, chunksize=65536):
    key = hashlib.sha256(key).digest()
    out_filename = in_filename+".enc"
    iv = get_random_bytes(16)
    mode = AES.MODE_CBC
    encryptor = AES.new(key,mode,iv)                                #AES 모드 설정
    filesize = os.path.getsize(in_filename)

    with open(in_filename,'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(key)
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' '*(16-len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

    os.unlink(in_filename)                                          #기존 파일 삭제
