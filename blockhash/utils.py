# encoding=utf8
"""set default encoding format"""

from __future__ import print_function
from __future__ import absolute_import
from future.standard_library import install_aliases
install_aliases()

# UTILITY FUNCTIONS

import hashlib

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


