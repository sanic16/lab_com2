from chat.models import cifrado_hill, descifrar_hill, enviar_hamming, recibir_hamming, char_bin, bin_char, descifrar_hill

cifrar_hill = cifrado_hill('Universidad de San Carlos de Guatemala')
data_bin = char_bin(cifrar_hill)

x = list() 
for i in data_bin:
    x.append(enviar_hamming(i))
    

data = list()
for i in x:
    data.append(recibir_hamming(i))

data = bin_char(data)
data = descifrar_hill(data)
print(data)

    

    