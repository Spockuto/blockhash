#!/usr/bin/env python

import hashlib
import sys
from multiprocessing import Pool 

def chunks( file_object , chunk_size=20971520):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def hashing(piece):
	return str(hashlib.sha224(piece).hexdigest())

if __name__ == '__main__':

	hashtree = ''

	big_file = open(sys.argv[1] ,'rb')
	pool = Pool(4)
	
	for chunk_hash in pool.imap(hashing, chunks(big_file)):
		hashtree = hashtree + chunk_hash

	print str(hashlib.sha224(hashtree).hexdigest())
	
	sys.exit()