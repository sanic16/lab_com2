

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


data = '0101001'
print(data)
# paso 1
r = num_bits_redundantes(len(data))
print(r)
# paso 2
arr = col_bits_redundantes(data, r)
print(arr)
# paso 3
bits_paridad = calc_bits_paridad(arr, r)
print(bits_paridad)
# paso 4
new_arr = insertar_bits_paridad(arr, bits_paridad, r)
print(new_arr)

print('-----------------------------\n\n')

new_arr = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1]
paridad_cal = calc_bits_paridad(new_arr, r)
print(paridad_cal)
paridad_ext = ext_bits_paridad(new_arr, r)
print(paridad_ext)
comparacion = comparar_paridad(paridad_cal, paridad_ext)
print(comparacion)
bin = binario_a_decimal(comparacion)
print(bin)
verificacion = verificar(new_arr, bin)
print(verificacion)
res = extraer_datos(verificacion, r)
print(res)