#!/usr/bin/env python

import hashlib
import sys
from multiprocessing import Pool
from argparse import ArgumentParser


#Default fixed size for chunks in 20Mb based on multiple experiments

parser = ArgumentParser()
parser.add_argument('-1', '--sha1', action='store_true')
parser.add_argument('-2', '--sha224', action='store_true')
parser.add_argument('-3', '--sha256', action='store_true')
parser.add_argument('-4', '--sha384', action='store_true')
parser.add_argument('-5', '--sha512', action='store_true')
parser.add_argument('-f', '--file' , type =str , help="The path to the file")
args = parser.parse_args()

def chunks( file_object , chunk_size=20971520):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def hashing1(piece):
	return str(hashlib.sha1(piece).hexdigest())

def hashing224(piece):
	return str(hashlib.sha224(piece).hexdigest())

def hashing256(piece):
	return str(hashlib.sha256(piece).hexdigest())

def hashing384(piece):
	return str(hashlib.sha384(piece).hexdigest())

def hashing512(piece):
	return str(hashlib.sha512(piece).hexdigest())


hashtree = ''

big_file = open(args.file ,'rb')
pool = Pool(4)

#SHA1
if args.sha1 :
	for chunk_hash in pool.imap(hashing1, chunks(big_file)):
		hashtree = hashtree + chunk_hash
	print str(hashlib.sha1(hashtree).hexdigest())

#SHA224
if args.sha224 :
	for chunk_hash in pool.imap(hashing224, chunks(big_file)):
		hashtree = hashtree + chunk_hash
	print str(hashlib.sha224(hashtree).hexdigest())

#SHA256
if args.sha256 :
	for chunk_hash in pool.imap(hashing256, chunks(big_file)):
		hashtree = hashtree + chunk_hash
	print str(hashlib.sha256(hashtree).hexdigest())

#SHA384
if args.sha384 :
	for chunk_hash in pool.imap(hashing384, chunks(big_file)):
		hashtree = hashtree + chunk_hash
	print str(hashlib.sha384(hashtree).hexdigest())

#SHA512
if args.sha512 :
	for chunk_hash in pool.imap(hashing512, chunks(big_file)):
		hashtree = hashtree + chunk_hash
	print str(hashlib.sha512(hashtree).hexdigest())


sys.exit()