#!/usr/bin/env python

import string

# alphabet of lowercase, upppercase, digits and space
alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + ' '

# vigenere cipher
def vigenere(msg, key, decrypt=False):
    # result
    result = ""
    # control whether to encrypt (add key) or decrypt (subtract key)
    mult = 1
    if decrypt:
        mult = -1
    # for each index and character at this index in message
    for i, c in enumerate(msg):
        # get current letter of key to use
        key_letter_to_use = key[i % len(key)]
        # character of result is index of message character in alphabet plus/minus index of key letter
        # in alphabet, mod 63 to wrap round if result is higher than length of alphabet
        result += alphabet[(alphabet.index(c) + (mult * alphabet.index(key_letter_to_use))) % 63]
    return result