import tkinter as tk
from turtle import back


root = tk.Tk()
text = tk.Text(root)
text.insert(tk.INSERT, "Hello.....")
text.insert(tk.END, "Bye Bye.....")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="white")

root.mainloop()