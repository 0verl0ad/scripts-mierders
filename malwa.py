#!/usr/bin/env python3

#Creado por @LuisGF (CyberpunK)

import base64
import sys
import gzip
import io
import zlib

from Crypto.Cipher import ARC4
from Crypto.Hash import MD5

def main():
    if len(sys.argv) != 3:
        print (" Usage: <domainfile> <key> ")
        return 1

    domain_file = sys.argv[1]
    key = bytes(sys.argv[2], 'utf-8')            
    md5key = MD5.new(key).digest()
    
    cipher = ARC4.new(md5key)
    
    with open(domain_file, 'rb') as f:
       data = f.read()
    
    # Decrypt RC4 Data
    data_dec = cipher.decrypt(data) 
    
    with open('decrypt', 'wb') as f:
        f.write(data_dec)
    
    print('Data writen to decrypt file.')
    
    # Añadimos la cabecera GZIP para que pueda ser descomprimido con gzip
    data2 = b"\x1f\x8b\x08\x00\x00\x00\x00\x00" + data_dec
   # data2 = data_dec
    with open('deflate.gz', 'wb') as f:
        f.write(data2)
        
    print('Data writen to deflate.gz file. Pleas use zcat')
    
    return 0

if __name__ == '__main__':      
    main()
