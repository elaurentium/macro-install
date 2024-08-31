import tkinter as tk
from tkinter import ttk
from controller.controlScript import execButton

def onSelection(event):
    global select
    select = event.widget.get()

def screen():
    root = tk.Tk()
    root.title("EXECUTOR SCRIPT")
    root.geometry("300x100")

    options = ["Script Completo", "Atualização", "XPTO"]
    input_options = ttk.Combobox(root, values=options)
    input_options.pack(pady=10)

    input_options.bind("<<ComboboxSelected>>", onSelection)

    button = ttk.Button(root, text="Executar", command=lambda: execButton(select))
    button.pack(pady=10)

    root.mainloop()

