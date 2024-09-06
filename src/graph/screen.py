import tkinter as tk
from tkinter import ttk
from controller.controlScript import execButton

def onSelection(event):
    global select
    select = event.widget.get()

def screen():
    root = tk.Tk()
    root.title("EXECUTOR SCRIPT")
    root.geometry("300x180")

    style = ttk.Style()
    style.configure('TButton', padding=10)
    style.configure('TCombox', padding=5)

    options = ["Script Completo", "Atualização", "XPTO"]
    input_options = ttk.Combobox(root, values=options)
    input_options.pack(pady=20, padx=10)

    input_options.bind("<<ComboboxSelected>>", onSelection)

    button_frame = tk.Frame(root)
    button_frame.pack(side='right', padx=10)

    browserButton = ttk.Button(button_frame, text="Procurar")
    browserButton.pack(side='top', pady=5)

    button = ttk.Button(button_frame, text="Executar", command=lambda: execButton(select))
    button.pack(side='top', pady=5)
    
    root.mainloop()

