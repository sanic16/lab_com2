import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Desencriptación Hill")
parser.add_argument("--msg", help="Desencripta el mensaje",
default="ANTRQVKVRMELIHVDLWRDGXTLTVIYDKKLFUDCWTV")
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
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
    ' ' : 26
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

# mapeando carácter-entero
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

# matríz llave
key = [[35, 53, 12], [12, 21, 5], [2, 4, 1]]

# inversa matríz llave
key_inv = np.linalg.inv(key)

# redondear al entero más cercano
key_inv = np.rint(key_inv)
key_inv = key_inv.astype(int)

# modulo 27 de matríz llave
key_inv_27 = key_inv%27

# multiplando matríz msg x key_inv_27
res = key_inv_27@msg

# calculando módulo 27 del producto
res = res%27

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


