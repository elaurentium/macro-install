import tkinter as tk
from tkinter import ttk
import json
import os
from controller.controlScript import *

PATH_FILE = r'.\src\paths\paths.json' if os.name == 'nt' else './src/paths/paths.json'

def load_paths():
    if os.path.exists(PATH_FILE):
        with open(PATH_FILE, 'r') as file:
            return json.load(file)
    return []

def save_path(paths):
    os.makedirs(os.path.dirname(PATH_FILE), exist_ok=True)
    with open(PATH_FILE, 'w') as file:
        json.dump(paths,file)

options = load_paths()

def onSelection(event):
    global select
    select = event.widget.get()


def updateOptions(option):
    new_option = search_button()

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

    button = ttk.Button(button_frame, text="Executar", command=lambda: controlScript.exec_button(select))
    button.pack(side='top', pady=5)
    
    root.mainloop()


