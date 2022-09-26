from chat.models import cifrado_hill, descifrar_hill, enviar_hamming, recibir_hamming, char_bin, bin_char, descifrar_hill
import tkinter as tk
from tkinter import ttk
"""
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
"""
def cifrar():
    texto_cifrado.set(cifrado_hill(texto_ingresar.get()))

def codificar_hamming():
    cifrado = texto_cifrado.get()
    # convertir a binario
    data_bin = char_bin(cifrado)
    data = list()
    for i in data_bin:
        data.append(enviar_hamming(i))
    cod_hamming.set(data)
    

def dec_hamming():
    cifrado = texto_cifrado.get()
    # convertir a binario
    data_bin = char_bin(cifrado)
    data = list()
    for i in data_bin:
        data.append(enviar_hamming(i))
    data_dec = list()
    for i in data:
        data_dec.append(recibir_hamming(i))
    data_dec = bin_char(data_dec)
    dec_hamming_var.set(data_dec)

def descifrar():
    texto_descifrar.set(descifrar_hill(dec_hamming_var.get()))



root = tk.Tk()
texto_ingresar = tk.StringVar()
texto_cifrado = tk.StringVar()
cod_hamming = tk.StringVar()
dec_hamming_var = tk.StringVar()
texto_descifrar = tk.StringVar()

label1 = tk.Label(root, text="Ingresar texto: ")
label1.grid(row=0, column=0, sticky=(tk.W + tk.E))
entry1 = tk.Entry(root, textvariable=texto_ingresar)
entry1.grid(row=0, column=1, sticky=(tk.W + tk.E))
button1 = tk.Button(root, text="Cifrar Texto", command=cifrar)
button1.grid(row=0, column=2, sticky=(tk.W + tk.E))

label2 = tk.Label(root, text="Cifrado Hill: ")
label2.grid(row=1, column=0, sticky=(tk.W + tk.E))
entry2 = tk.Entry(root, textvariable=texto_cifrado)
entry2.grid(row=1, column=1, sticky=(tk.W + tk.E))
button2 = tk.Button(root, text="Codificar Hamming", command=codificar_hamming)
button2.grid(row=1, column=2, sticky=(tk.W + tk.E))

label3 = tk.Label(root, text="Hamming codificado: ")
label3.grid(row=2, column=0, sticky=(tk.W + tk.E))
entry3 = tk.Entry(root, textvariable=cod_hamming)
entry3.grid(row=2, column=1, sticky=(tk.W + tk.E))
button3 = tk.Button(root, text="Decodificar Hamming", command=dec_hamming)
button3.grid(row=2, column=2, sticky=(tk.W + tk.E))

label4 = tk.Label(root, text="Hamming decodificado: ")
label4.grid(row=3, column=0, sticky=(tk.W + tk.E))
entry4 = tk.Entry(root, textvariable=dec_hamming_var)
entry4.grid(row=3, column=1, sticky=(tk.W + tk.E))
button4 = tk.Button(root, text="Descifrar", command=descifrar)
button4.grid(row=3, column=2, sticky=(tk.W + tk.E))

label5 = tk.Label(root, text="Descifrado Hill: ")
label5.grid(row=4, column=0, sticky=(tk.W + tk.E))
entry5 = tk.Entry(root, textvariable=texto_descifrar)
entry5.grid(row=4, column=1, sticky=(tk.W + tk.E))




root.mainloop()

    

    