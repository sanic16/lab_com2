import tkinter as tk

root = tk.Tk()
root.resizable(width=False, height=False)

def send():
    text.insert('1.0', 'here is my my\ntext to insert')

def send2():
    text.insert('2.0', 'Hola, que tal amigo')

def retrieve():
    the_text = text.get('1.0', 'end')
    my_text_label.set(the_text)

my_text_label = tk.StringVar()

text = tk.Text(root, width=80, height=30, foreground='red', background='sky blue', padx=10, relief=tk.RIDGE)
text.pack()
send_button = tk.Button(root, text="Send User1", command=send)
send_button.pack()
send_button2 = tk.Button(root, text="Send User2", command=send2)
send_button2.pack()
retrieve_button = tk.Button(root, text="Retrieve", command=retrieve)
retrieve_button.pack()

label = tk.Label(root, textvariable=my_text_label)
label.pack()
root.mainloop()