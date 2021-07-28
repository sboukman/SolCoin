#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:13:32 2021

@author: sollyboukman
"""
from backend.wallet.wallet import Wallet

def test_verify_valid_signature():
    data = {'foo': 'Test_data'}
    wallet = Wallet()
    signature = wallet.sign(data)
    
    assert Wallet.verify(wallet.public_key, data, signature)
    
def test_verify_invalid_signature():
    data = {'foo': 'Test_data'}
    wallet = Wallet()
    signature = wallet.sign(data)
    
    assert not Wallet.verify(Wallet().public_key, data, signature)

