#!/usr/bin/env python
import hashlib
from multiprocessing import Pool
import multiprocessing
from argparse import ArgumentParser

#Default fixed size for chunks in 20Mb based on multiple experiments

parser = ArgumentParser()
parser.add_argument('-1', '--sha1', action='store_true')
parser.add_argument('-2', '--sha224', action='store_true')
parser.add_argument('-3', '--sha256', action='store_true')
parser.add_argument('-4', '--sha384', action='store_true')
parser.add_argument('-5', '--sha512', action='store_true')
parser.add_argument('-f', '--file', type=str, help="The path to the file")
args = parser.parse_args()

def chunks(file_object, chunk_size=20971520):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def hashing(piece):
    if args.sha1:
        return str(hashlib.sha1(piece).hexdigest())
    elif args.sha224:
        return str(hashlib.sha224(piece).hexdigest())
    elif args.sha256:
        return str(hashlib.sha256(piece).hexdigest())
    elif args.sha384:
        return str(hashlib.sha384(piece).hexdigest())
    elif args.sha512:
        return str(hashlib.sha512(piece).hexdigest())
    else:
    	raise ValueError('Specify a Hash function')

hashtree = ''

big_file = open(args.file, 'rb')
pool = Pool(multiprocessing.cpu_count())

for chunk_hash in pool.imap(hashing, chunks(big_file)):
    hashtree = hashtree + chunk_hash

print str(hashing(hashtree))
pool.terminate() 
