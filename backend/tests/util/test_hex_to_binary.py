#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 06:05:52 2021

@author: sollyboukman
"""

from backend.util.hex_to_binary import hex_to_binary

def test_hex_to_binary():
    original_number = 789
    hex_number = hex(original_number)[2:]
    binary_number = hex_to_binary(hex_number) 
    
    assert int(binary_number, 2) == original_number
    

