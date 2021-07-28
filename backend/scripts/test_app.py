#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 17:55:22 2021

@author: sollyboukman
"""

import requests

def get_blockchain():
    return requests.get('http://localhost:5000/blockchain').json()

start_blockchain = get_blockchain()

print(f'start_blockchain: {start_blockchain}')