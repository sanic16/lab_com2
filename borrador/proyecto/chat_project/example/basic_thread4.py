from email.policy import strict
import tkinter as tk
import serial
import threading
import datetime
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = "/dev/ttyUSB1"
ser.open()
read = True
datos = ""

def serialEvent():
    global ser, read, datos
    
    while read is True:
        time.sleep(1)
        datos = ser.read_until().decode('latin1')
        datos = str(datetime.datetime.now()) + "-" + "Julio " + datos
        text.insert(tk.END, datos)
        text.tag_add("here", "end", "end - 26 chars")
        text.tag_config("here", background="gray", foreground="red")
    return

def enviar(event):
    data = var.get()
    data = data + "\n"
    ser.write(data.encode(encoding="latin1"))
    var.set('')
    text.see('end')

root = tk.Tk()

# Creating ScrollBars
scrolly = tk.Scrollbar(root)
scrolly.grid(row=0, column=1)


# Creating Text Widget
text = tk.Text(root, width=80, height=14, undo=True, yscrollcommand=scrolly.set)
text.grid(row=0)
scrolly.config(command=text.yview)
t = threading.Thread(target=serialEvent)
t.start()

var = tk.StringVar()

frame = tk.Frame(root)
entry = tk.Entry(frame, textvariable=var)
entry.grid(row=0, column=0, sticky=(tk.W + tk.E))

entry.bind("<Return>", enviar)

button = tk.Button(frame, text="Enviar", command=enviar)
button.grid(row=0, column=1, sticky=(tk.W + tk.E))
frame.grid(row=1, sticky=(tk.W + tk.E))
frame.columnconfigure(0, weight=1)

root.mainloop()