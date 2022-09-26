# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:39:59 2022

@author: DELL
"""

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 "

letter_to_index = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'Ñ': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26,
        'a': 27,
        'b': 28,
        'c': 29,
        'd': 30,
        'e': 31,
        'f': 32,
        'g': 33,
        'h': 34,
        'i': 35,
        'j': 36,
        'k': 37,
        'l': 38,
        'm': 39,
        'n': 40,
        'ñ': 41,
        'o': 42,
        'p': 43,
        'q': 44,
        'r': 45,
        's': 46,
        't': 47,
        'u': 48,
        'v': 49,
        'w': 50,
        'x': 51,
        'y': 52,
        'z': 53,
        '!': 54,
        '"': 55,
        '#': 56,
        '$': 57,
        '%': 58,
        '&': 59,
        '(': 60,
        ')': 61,
        '*': 62,
        '+': 63,
        ',': 64,
        '-': 65,
        '.': 66,
        '/': 67,
        '0': 68,
        '1': 69,
        '2': 70,
        '3': 71,
        '4': 72,
        '5': 73,
        '6': 74,
        '7': 75,
        '8': 76,
        '9': 77,
        ':': 78,
        ';': 79,
        '<': 80,
        '=': 81,
        '>': 82,
        '?': 83,
        '@': 84,
        '[': 85,
        ']': 86,
        '^': 87,
        '_': 88,
        ' ': 89
    }

k = letter_to_index.keys()
v = letter_to_index.values()
 

index_to_letter = dict(zip(v,k))


def encrypt(message, key):
    encrypted = ""
    split_message = [
        message[i : i + len(key)] for i in range(0, len(message), len(key))
    ]
    print(split_message)

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(index_to_letter)
            encrypted += index_to_letter[number]
            i += 1

    return encrypted


def decrypt(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(letter_to_index)
            decrypted += index_to_letter[number]
            i += 1

    return decrypted


def main():

    message = input("Ingrese texot a cifrar:")
    key = input("Ingrese key:")

    
    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)

    print("Original message: " + message)
    print("Encrypted message: " + encrypted_message)
    print("Decrypted message: " + decrypted_message)
    


main()