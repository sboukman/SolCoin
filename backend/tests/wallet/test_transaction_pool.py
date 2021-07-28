#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:10:28 2021

@author: sollyboukman
"""

from backend.wallet.transaction_pool import TransactionPool
from backend.wallet.transaction import Transaction
from backend.wallet.wallet import Wallet

def test_set_transaction():
    transaction_pool = TransactionPool()
    
    transaction = Transaction(Wallet(), 'recipient', 1)
    transaction_pool.set_transaction(transaction)
    
    assert transaction_pool.transaction_map[transaction.id] == transaction 