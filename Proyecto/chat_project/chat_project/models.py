
import numpy as np
from .constants import EncryptionTypes

def cifrar(type, msg):
    if type == EncryptionTypes[1]:
        return cifrado_hill(msg)
    elif type == EncryptionTypes[2]:
        return encrypt(msg, key="lab")
    elif type == EncryptionTypes[0]:
        return caesar_encrypt(msg, 3)

def descifrar(type, msg):
    if type == EncryptionTypes[1]:
        return descifrar_hill(msg)
    elif type == EncryptionTypes[2]:
        return decrypt(msg, key="lab")
    elif type == EncryptionTypes[0]:
        return caesar_decrypt(msg, 3)

def cifrado_hill(msg):
# Matriz llave 3x3, tiene que ser inversible
    key = [[35, 53, 12], [12, 21, 5], [2, 4, 1]]

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

    """
    Se complementa con espacios si el mensaje no es divisible
    por 3
    """
    pad = len(msg)%3
    if len(msg)%3!=0:
        for x in range(3-pad):
            msg += '#'

    # se crea una lista de elementos tipo str de 3 caracteres
    i = 0
    my_list = list()
    while(i<len(msg)):
        my_list.append(msg[i:(i+3)])
        i+=3
    #print(my_list)

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
            else:
                z.append(chars[k])
            i+=1

    #print(x)
    #print(y)
    #print(z)


    key = np.array(key)
    #print(key)

    msg = np.array([x,y,z])
    #print(msg)

    # Multiplicando matriz mensaje por clave
    res = key@msg
    #print(res)

    # Aplicando modulo len(chars)
    res = np.mod(res, len(chars))
    k = chars.keys()
    v = chars.values()
    #print(res)

    # Invirtiendo el diccionario
    d_chars = dict(zip(v,k))
    #print(d_chars)

    # Dividiendo la matriz en listas
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

    #print(x)
    #print(y)
    #print(z)

    # mapeando de enteros a caracteres
    msg = ''
    for j in range(len(x)):
        msg += d_chars[x[j]] + d_chars[y[j]] + d_chars[z[j]]
        

    # texto cifrado
    return msg


def descifrar_hill(msg):
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
    i=0 
    my_list = list()
    while(i<len(msg)):
        my_list.append(msg[i:(i+3)])
        i+=3
    x = list()
    y = list()
    z = list()

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

    key = [[35, 53, 12], [12, 21, 5], [2, 4, 1]]

    key_inv = np.linalg.inv(key)
    key_inv = np.rint(key_inv)
    key_inv = key_inv.astype(int)
    key_inv_27 = key_inv%len(chars)
    res = key_inv_27@msg
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
    return msg

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

def caesar_encrypt(msg, index):
    d = index%len(letter_to_index)
    text = ""
    for i in msg:
        number = (letter_to_index[i] + d)%(len(letter_to_index))
        text += index_to_letter[number]
    return text

def caesar_decrypt(msg, index):
    d = index%len(letter_to_index)
    text = ""
    for i in msg:
        number = (letter_to_index[i] - d)%(len(letter_to_index))
        text += index_to_letter[number]
    return text

def num_bits_redundantes(m):
    for i in range(m):
        if(2**i >= m + i + 1):
            return i

def col_bits_redundantes(data, r):

    j= 0
    k = 0
    m = len(data)
    res = ''

    for i in range(1, m + r+1):
        if(i==2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[k]
            k += 1
    return res

def calc_bits_paridad(arr, r):
    bits_paridad = []

    for i in [2**x for x in range(r)]:
        var = 0
        for j in range(1, len(arr) + 1):
            if (j not in [2**x for x in range(r)]):
                #sublist.append(int(arr[j-1]))
                if j&i:
                    var += int(arr[j-1])

        bits_paridad.append(var%2)
    return bits_paridad

def insertar_bits_paridad(arr, bits_paridad, r):
    my_iter = iter(bits_paridad)
    new_arr = []
    for j in range(1, 1 + len(arr)):
        if (j not in [2**x for x in range(r)]):
            new_arr.append(int(arr[j-1]))
        else:
            new_arr.append(next(my_iter))
    return new_arr

def ext_bits_paridad(arr, r):
    newlist = []

    
    for i in [2**x for x in range(r)]:
        newlist.append(int(arr[i-1]))
    return newlist  

def comparar_paridad(paridad_cal, paridad_ext):
    comparacion = list()
    for i in range(0, len(paridad_cal)):
        if paridad_cal[i] == paridad_ext[i]:
            comparacion.append(0)
        else:
            comparacion.append(1)

    return comparacion 

def binario_a_decimal(arr):
    val = 0
    for i in range(0, len(arr)):
        if arr[i] == 1:
            
            val += 2**i
    
    return val

def verificar(arr, dec):
    if dec == 0:
        return arr
    else:
        arr[dec-1] = (0 if arr[dec-1]==1  else 1)
    return arr

def extraer_datos(arr, r):
    res = ''
    par = [2**x - 1 for x in range(r)]
    for i in range(0,len(arr)):
        if i not in par:
            res += str(arr[i])
    return res


def enviar_hamming(data):
    r = num_bits_redundantes(len(data))
    arr = col_bits_redundantes(data, r)
    bits_paridad = calc_bits_paridad(arr, r)
    new_arr = insertar_bits_paridad(arr, bits_paridad, r)
    return new_arr

def recibir_hamming(data):
    r = num_bits_redundantes(len(data))
    paridad_cal = calc_bits_paridad(data, r)
    paridad_ext = ext_bits_paridad(data, r)
    comparacion = comparar_paridad(paridad_cal, paridad_ext)
    bin = binario_a_decimal(comparacion)
    verificacion = verificar(data, bin)
    res = extraer_datos(verificacion, r)
    return res

chars = {
        'A': '0000000',
        'B': '0000001',
        'C': '0000010',
        'D': '0000011',
        'E': '0000100',
        'F': '0000101',
        'G': '0000110',
        'H': '0000111',
        'I': '0001000',
        'J': '0001001',
        'K': '0001010',
        'L': '0001011',
        'M': '0001100',
        'N': '0001101',
        'Ñ': '0001110',
        'O': '0001111',
        'P': '0010000',
        'Q': '0010001',
        'R': '0010010',
        'S': '0010011',
        'T': '0010100',
        'U': '0010101',
        'V': '0010110',
        'W': '0010111',
        'X': '0011000',
        'Y': '0011001',
        'Z': '0011010',
        'a': '0011011',
        'b': '0011100',
        'c': '0011101',
        'd': '0011110',
        'e': '0011111',
        'f': '0100000',
        'g': '0100001',
        'h': '0100010',
        'i': '0100011',
        'j': '0100100',
        'k': '0100101',
        'l': '0100110',
        'm': '0100111',
        'n': '0101000',
        'ñ': '0101001',
        'o': '0101010',
        'p': '0101011',
        'q': '0101100',
        'r': '0101101',
        's': '0101110',
        't': '0101111',
        'u': '0110000',
        'v': '0110001',
        'w': '0110010',
        'x': '0110011',
        'y': '0110100',
        'z': '0110101',
        '!': '0110110',
        '"': '0110111',
        '#': '0111000',
        '$': '0111001',
        '%': '0111010',
        '&': '0111011',
        '(': '0111100',
        ')': '0111101',
        '*': '0111110',
        '+': '0111111',
        ',': '1000000',
        '-': '1000001',
        '.': '1000010',
        '/': '1000011',
        '0': '1000100',
        '1': '1000101',
        '2': '1000110',
        '3': '1000111',
        '4': '1001000',
        '5': '1001001',
        '6': '1001010',
        '7': '1001011',
        '8': '1001100',
        '9': '1001101',
        ':': '1001110',
        ';': '1001111',
        '<': '1010000',
        '=': '1010001',
        '>': '1010010',
        '?': '1010011',
        '@': '1010100',
        '[': '1010101',
        ']': '1010110',
        '^': '1010111',
        '_': '1011000',
        ' ': '1011001'
    }

def char_bin(data):
    
    msg = []
    for x in data:
        msg.append(chars[x])
    return msg

def bin_char(data):
    k = chars.keys()
    v = chars.values()

    d_chars = dict(zip(v,k))
    msg = ''

    for x in data:
        msg += d_chars[x]
    
    return msg

def codificar_hamming(msg):
    data_bin = char_bin(msg)
    data = list()
    for i in data_bin:
        data.append(enviar_hamming(i))
    new_data = ''

    for dat in data:
        for i in dat:
            if i == 0:
                new_data+='0'
            else:
                new_data+='1'
    return new_data

def dec_hamming(msg):
    list_t = []
    i = 0
    while i<len(msg):
        m = list(msg[i:i+11])
        new_list = []
        for x in m:
            new_list.append(int(x))
        list_t.append(new_list)
        i+=11
    data_dec = list()
    for i in list_t:
        data_dec.append(recibir_hamming(i))
    data_dec = bin_char(data_dec)
    return data_dec


