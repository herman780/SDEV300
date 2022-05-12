# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:07:38 2022
Lab 4 (part 2): Generating ten (10) passwords with different hashing
algorithms, and then using a popular online password cracking website
to see if the passwords can be cracked
@author: Herman Mann
"""

import hashlib
# input a message to encode
print('Enter a message to encode:')
message = input()
# encode it to bytes using UTF-8 encoding
message = message.encode()
# hash with MD5 (very weak)
print("MD5:", hashlib.md5(message).hexdigest())
# Lets try a stronger SHA-2 family
print("SHA256:", hashlib.sha256(message).hexdigest())
print("SHA512:", hashlib.sha512(message).hexdigest())

#Generating 10 different passwords using different hashing algorithms
print("blake2s:", hashlib.blake2s(message).hexdigest())
print("SHA384:", hashlib.sha384(message).hexdigest())
print("blake2b:", hashlib.blake2b(message).hexdigest())
print("SHA1:", hashlib.sha1(message).hexdigest())
print("SHA3_224:", hashlib.sha3_224(message).hexdigest())
print("SHA3_384:", hashlib.sha384(message).hexdigest())
print("SHA3_512:", hashlib.sha3_512(message).hexdigest())
