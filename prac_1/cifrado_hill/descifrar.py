import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Cifrado Hill")
parser.add_argument("--msg", help="Desencripta el mensaje",
default=">c0m!UBxkSk$3PD,Ue<)UE2O)*IB5-rEr")
args = parser.parse_args()

# mensaje a descifrar
msg = args.msg

chars = {
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




# se crea una lista de elementos tipo str de 3 caracteres

i=0 
my_list = list()
while(i<len(msg)):
    my_list.append(msg[i:(i+3)])
    i+=3
print(my_list)

# Matrices 1-D
x = list()
y = list()
z = list()

# mapeando caracter-entero
for in_list in my_list:
    i = 0
    for k in in_list:
        if i==0:
            x.append(chars[k])
        elif i==1:
            y.append(chars[k])
        elif i==2:
            z.append(chars[k])
        i+=1

msg = np.array([x,y,z])

# matriz llave
key = [[35, 53, 12], [12, 21, 5], [2, 4, 1]]

# inversa matriz llave
key_inv = np.linalg.inv(key)

# redondear al entero mas cercano
key_inv = np.rint(key_inv)
key_inv = key_inv.astype(int)

# modulo 27 de matriz llave
key_inv_27 = key_inv%len(chars)

# multiplando matriz msg x key_inv_27
res = key_inv_27@msg

# calculando modulo 27 del producto
res = res%len(chars)

k = chars.keys()
v = chars.values()
d_chars = dict(zip(v,k))

x = list()
y = list()
z = list()

i=0
for in_list in res:
    for k in in_list:
        if i == 0:
            x.append(k)
        elif i == 1:
            y.append(k)
        elif i == 2:
            z.append(k)
    i+=1

msg = ''
i=0
for j in range(len(x)):
    msg += d_chars[x[j]] + d_chars[y[j]] + d_chars[z[j]]
    i+=1
print(msg)


