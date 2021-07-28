#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 03:01:47 2021

@author: sollyboukman
"""
import hashlib
import json



def crypto_hash(*args):
    """
    Return a sha-256 hash of given arguments
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))

    joined_data = ''.join(stringified_args)
    
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")
    print(f"crypto_hash(2, 'one', [3]): {crypto_hash(2, 'one', [3])}")
    
if __name__ == '__main__':
    main()