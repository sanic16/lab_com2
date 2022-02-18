import numpy as np
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

# mensaje a enviar
test_str = 'UNIVERSIDAD DE SAN CARLOS DE GUATEMALA'

"""
Se complementa con espacios si el mensaje no es divisible
por 3
"""
extra = len(test_str)%3
for x in range(3-extra):
    test_str += ' '

"""
Se crea una lista de Strings de 3 carácteres y usando
mapeo se obtiene el entero equivalente
"""
i = 0
my_list = list()
while(i<len(test_str)):
    my_list.append(test_str[i:(i+3)])
    i+=3
print(my_list)

# Matrices 1-D 
x = list()
y = list()
z = list()

"""
Se mapea de string a entero y se agregan los elementos
a la matriz 1-D
"""
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
print(x)
print(y)
print(z)

# Matríz llave 3x3, tiene que ser inversible
key = [[35, 53, 12], [12, 21, 5], [2, 4, 1]]

key = np.array(key)
msg = np.array([x,y,z])
# Multiplicando matríz mensaje por clave
res = key@msg
print(res)
# Aplicando modulo len(chars)
res = np.mod(res, len(chars))
print(res)
k = chars.keys()
v = chars.values()
d_chars = dict(zip(v,k))
print(d_chars)


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

