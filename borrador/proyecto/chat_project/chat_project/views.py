import tkinter as tk
from tkinter import messagebox


class MainMenu(tk.Menu):
    """The Application's main menu"""

    def __init__(self, parent, settings, callbacks, EncryptionTypes, **kwargs):

        
        super().__init__(parent, **kwargs)

        # file menu
        file_menu = tk.Menu(self, tearoff=False)
        file_menu.add_command(
            label="Seleccionar archivo...",
            command=callbacks['file->open']
        )
        file_menu.add_separator()
        file_menu.add_command(label="Salir", 
            command=callbacks['file->quit']
        )
        self.add_cascade(label='Archivo', menu=file_menu)

        # options menu
        options_menu = tk.Menu(self, tearoff=False)
        options_menu.add_checkbutton(label="CRC Hamming")
        self.add_cascade(label='Opciones', menu=options_menu)

        encryption_menu = tk.Menu(options_menu, tearoff=False)
        options_menu.add_cascade(label="Encryption", menu=encryption_menu)



        # help menu
        help_menu = tk.Menu(self, tearoff=False)
        help_menu.add_command(label="About", command=self.show_about)
        self.add_cascade(label="Ayuda", menu=help_menu)

        for i in EncryptionTypes:
            encryption_menu.add_radiobutton(label="{} encryption".format(i), value=i, variable=settings['encriptacion'])
    
    def show_about(self):
        """Show the about dialog"""
        about_message = 'Aplicación de Chat'
        about_detail = ('Por Julio Sanic 2012-22286 y\nMike Medina 2019-03908\n'
        'Para asistencia contacte al autor')
        messagebox.showinfo(title="About", message=about_message, detail=about_detail)