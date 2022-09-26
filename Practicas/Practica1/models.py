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
    
    k = chars.keys()
    v = chars.values()
    d_chars = dict(zip(v,k))
    print()
    print("Letra: ", d_chars[data], " ", data)
    r = num_bits_redundantes(len(data))
    print(r)
    arr = col_bits_redundantes(data, r)
    print(arr)
    bits_paridad = calc_bits_paridad(arr, r)
    print(bits_paridad)
    new_arr = insertar_bits_paridad(arr, bits_paridad, r)
    print(new_arr)
    return new_arr

def recibir_hamming(data):
    
    r = num_bits_redundantes(len(data))
    print("Calculo de Bits de paridad")
    print(r)
    
    paridad_cal = calc_bits_paridad(data, r)
    print("Paridad calculada")
    print(paridad_cal)
    paridad_ext = ext_bits_paridad(data, r)
    print("Paridad extraída")
    print(paridad_ext)
    comparacion = comparar_paridad(paridad_cal, paridad_ext)
    print("Comparación")
    print(comparacion)
    bin = binario_a_decimal(comparacion)
    print("Bit de error")
    print(bin)
    verificacion = verificar(data, bin)
    print("Verificación")
    print(verificacion)
    res = extraer_datos(verificacion, r)
    print("Extraer datos")
    print(res)
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
    # --------------------------------
    print("Frase o letra a aplicar hamming")
    print(msg)
    # -------------------------------
    print("Texto decodificado a binario")
    data_bin = char_bin(msg)
    print(data_bin)
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
    print(new_data)
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
    letra = 1
    for i in list_t:
        print()
        print("letra " + str(letra))
        letra += 1
        data_dec.append(recibir_hamming(i))

    data_dec = bin_char(data_dec)
    return data_dec
