import threading
import tkinter as tk
from tkinter import ttk
from . import views as v
from . import models as m
from .constants import EncryptionTypes as ET
import datetime
import serial
import time



class Application(tk.Tk):
    """Application root window"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ser = serial.Serial()
        self.ser.baudrate = 9600
        self.ser.port = "/dev/ttyUSB0"
        #self.ser.open()
        self.read = True
        self.datos = ""

        self.var = tk.StringVar()

        self.title("HP-pc")
        self.resizable(width=False, height=False)

        self.settings = {
            'encriptacion': tk.StringVar(),
            'hamming': tk.BooleanVar()
        }
        
        self.callbacks = {
            'file->open': self.on_file_select,
            'file->quit': self.quiting
        }

        self.settings['encriptacion'].trace('w', self.show)
        

        menu = v.MainMenu(self, self.settings, self.callbacks, ET)
        self.config(menu=menu)

        self.text = tk.Text(self, width=60, height=20, bg="midnight blue", fg="white")
        self.text.grid(row=0, sticky=(tk.W + tk.E))

        self.my_frame = tk.Frame(self)
        self.my_frame.columnconfigure(0, weight=1)
        
        self.my_entry = tk.Entry(self.my_frame, textvariable=self.var)
        self.my_entry.bind("<Return>", self.send)
        self.my_entry.grid(row=0, column=0, sticky=(tk.W + tk.E + tk.N + tk.S))
        
        self.my_frame.grid(row=1, sticky=(tk.W + tk.E), pady=5)

        self.t = threading.Thread(target=self.serialEvent)
        self.t.start()

        self.columnconfigure(0, weight=1)


    def on_file_select(self):
        pass


    def send(self, event):
        data = self.var.get()
        data2 = "[HP-pc] " + data + "\n"

        """if self.settings['encriptacion'].get() == ET[1]:
            data = m.cifrar(ET[1], data)
        elif self.settings['encriptacion'].get() == ET[2]:
            data = m.cifrar(ET[2], data)
        elif self.settings['encriptacion'].get() == ET[0]:
            data = m.cifrar(ET[0], data)"""
        
        if self.settings['hamming'].get():
            data = m.codificar_hamming(data)
        
        data = data + "\n"
        self.ser.write(data.encode(encoding="latin1"))
        self.text.insert(tk.END, data2)
        self.var.set('')
        self.text.see('end')
    
    
    def serialEvent(self):
        
        while self.read is True:
            time.sleep(1)
            self.datos = self.ser.read_until().decode('latin1')
            self.datos = self.datos[0:-1]

            if self.settings['hamming'].get():
                self.datos = m.dec_hamming(self.datos)

            """if self.settings['encriptacion'].get() == ET[1]:
                self.datos = m.descifrar(ET[1], self.datos)
            elif self.settings['encriptacion'].get() == ET[2]:
                self.datos = m.descifrar(ET[2], self.datos)
            elif self.settings['encriptacion'].get() == ET[0]:
                self.datos = m.descifrar(ET[0], self.datos)"""
            

            self.datos = "[Samsung-pc] " + self.datos + "\n"
            self.text.insert(tk.END, self.datos)
            self.text.see('end')
        return
    
    def quiting(self):
        self.read = False
        self.quit()
        self.ser.close()
        exit()

    def show(self, *args):
        print(self.settings['encriptacion'].get())

    