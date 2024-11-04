import tkinter as tk
from tkinter import ttk
from controller.controlScript import execButton, searchButton
from controller.paths import load_paths, save_path

options = load_paths()

def onSelection(event):
    global select
    select = event.widget.get()


def updateOptions(option):
    new_option = searchButton()

    options.append(new_option)

    new_val = list(set(options))

    option['values'] = new_val

    save_path(new_val)

def screen():
    root = tk.Tk()
    root.title("EXECUTOR SCRIPT")
    root.geometry("300x180")

    style = ttk.Style()
    style.configure('TButton', padding=10)
    style.configure('TCombox', padding=5)

    input_options = ttk.Combobox(root, values=options)
    input_options.pack(pady=20, padx=10)

    input_options.bind("<<ComboboxSelected>>", onSelection)

    button_frame = tk.Frame(root)
    button_frame.pack(side='right', padx=10)

    browserButton = ttk.Button(button_frame, text="Procurar", command=lambda: updateOptions(input_options))
    browserButton.pack(side='top', pady=5)

    button = ttk.Button(button_frame, text="Executar", command=lambda: execButton(select))
    button.pack(side='top', pady=5)
    
    root.mainloop()


