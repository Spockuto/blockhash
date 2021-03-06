"""set default encoding format"""
from __future__ import print_function
from __future__ import absolute_import
from future.standard_library import install_aliases
install_aliases()

import sys
import os
import hashlib
from argparse import ArgumentParser
import multiprocessing
from multiprocessing import Pool
20971520
#Default fixed size for chunks in 20Mb based on multiple experiments
def chunks(file_object, chunk_size):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data + ":chunk"

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

def main():

    parser = ArgumentParser(description="Speed up your SHA. A different hash style.")
    parser.add_argument('-1', '--sha1', action='store_true')
    parser.add_argument('-2', '--sha224', action='store_true')
    parser.add_argument('-3', '--sha256', action='store_true')
    parser.add_argument('-4', '--sha384', action='store_true')
    parser.add_argument('-5', '--sha512', action='store_true')
    parser.add_argument('-f', '--file', type=str, help="The path to the file")
    parser.add_argument('-s', '--size', type=int, help="The size of the chunks")

    if len(sys.argv) == 1:
        parser.print_help()
        return

    global args
    args = parser.parse_args()

    if not args.size:
        args.size =  20971520
        
    hashtree = ''

    big_file = open(args.file, 'rb')
    pool = Pool(multiprocessing.cpu_count())

    for chunk_hash in pool.imap(hashing, chunks(big_file, args.size)):
        hashtree += chunk_hash + ":hash"
    pool.terminate()

    print(str(hashing(hashtree.encode('ascii'))))


if __name__ == '__main__':
    main()

