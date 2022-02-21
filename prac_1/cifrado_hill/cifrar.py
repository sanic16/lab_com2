import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Encriptación Hill')
parser.add_argument("--msg", 
help="Encripta el mensaje", 
default="UNIVERSIDAD DE SAN CARLOS DE GUATEMALA")
args = parser.parse_args()

# mensaje a cifrar
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


"""
Se complementa con espacios si el mensaje no es divisible
por 3
"""
pad = len(msg)%3
for x in range(3-pad):
    msg += ' '


# se crea una lista de elementos tipo str de 3 carácteres

i = 0
my_list = list()
while(i<len(msg)):
    my_list.append(msg[i:(i+3)])
    i+=3

# Matrices 1-D 
x = list()
y = list()
z = list()


# mapeando carácter-entero
for in_list in my_list:
    i = 0
    for k in in_list:
        if i==0:
            x.append(chars[k[0]])
        elif i==1:
            y.append(chars[k[0]])
        else:
            z.append(chars[k[0]])
        i+=1


# Matríz llave 3x3, tiene que ser inversible
key = [[35, 53, 12], [12, 21, 5], [2, 4, 1]]

key = np.array(key)
msg = np.array([x,y,z])
# Multiplicando matríz mensaje por clave
res = key@msg

# Aplicando modulo len(chars)
res = np.mod(res, len(chars))
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

# Mensaje a enviar
msg = ''
i=0
for j in range(len(x)):
    msg += d_chars[x[j]] + d_chars[y[j]] + d_chars[z[j]]
    i+=1
print(msg)

