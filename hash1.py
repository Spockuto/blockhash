#!/usr/bin/env python

import hashlib
import sys

def chunks( file_object , chunk_size=20971520):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data
if __name__ == '__main__':

	big_file = open(sys.argv[1] ,'rb')
	hashtree = []
	
	for piece in chunks(big_file):
		hashtree.append(str(hashlib.sha224(piece).hexdigest()))
	
	print hashtree