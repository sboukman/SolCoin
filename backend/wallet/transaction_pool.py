#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 21:56:48 2021

@author: sollyboukman
"""

class TransactionPool:
    def __init__(self):
        self.transaction_map = {}
        
    def set_transaction(self, transaction):
        """
        Set a transaction in the transaction pool.
        """
        self.transaction_map[transaction.id] = transaction
        
    def existing_transaction(self, address):
        """
        Find a transaction generated by the address in the transaction pool
        """
        for transaction in self.transaction_map.values():
            if transaction.input['address'] == address:
                return transaction
    def transaction_data(self):
        """
        Returns the transactions of the transaction pool represented in their
        json serialized form.
        """
        
        transaction_values = self.transaction_map.values()
    
        transaction_data = list(map(lambda transaction: transaction.to_json(), transaction_values))
        
        return transaction_data