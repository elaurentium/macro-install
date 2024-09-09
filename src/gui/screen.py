import tkinter as tk
from tkinter import ttk
import json
import os
from controller.controlScript import ControScript

PATH_FILE = 'paths.json'

class Screen:
    @staticmethod
    def load_paths():
        if os.path.exists(PATH_FILE):
            with open(PATH_FILE, 'r') as file:
                return json.load(file)
        return []
    
    @staticmethod
    def save_path(paths):
        with open(PATH_FILE, 'w') as file:
            json.dump(paths,file)


    options = load_paths()

    @staticmethod
    def onSelection(event):
        global select
        select = event.widget.get()

    @staticmethod
    def updateOptions(option):
        new_option = ControScript.searchButton()

        Screen.options.append(new_option)

        new_val = list(set(Screen.options))

        option['values'] = new_val

        Screen.save_path(new_val)
    
    @staticmethod
    def screen():
        root = tk.Tk()
        root.title("EXECUTOR SCRIPT")
        root.geometry("300x180")

        style = ttk.Style()
        style.configure('TButton', padding=10)
        style.configure('TCombox', padding=5)

        input_options = ttk.Combobox(root, values=Screen.options)
        input_options.pack(pady=20, padx=10)

        input_options.bind("<<ComboboxSelected>>", Screen.onSelection)

        button_frame = tk.Frame(root)
        button_frame.pack(side='right', padx=10)

        browserButton = ttk.Button(button_frame, text="Procurar", command=lambda: Screen.updateOptions(input_options))
        browserButton.pack(side='top', pady=5)

        button = ttk.Button(button_frame, text="Executar", command=lambda: ControScript.execButton(select))
        button.pack(side='top', pady=5)
        
        root.mainloop()


