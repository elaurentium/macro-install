import subprocess
import os
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from pathlib import Path

options = []

class ControScript:
    @staticmethod
    def execScript(scriptPath):
        script_path = Path(scriptPath)

        if not script_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {script_path}")
        
        ext = os.path.splitext(script_path)[1].lower()

        if ext == '.cmd':
            command = f'cmd /c start cmd /k "{script_path}"'
        else:
            command = f'cmd /c start powershell -NoExit -File "{script_path}"'
        
        try:
            result = subprocess.Popen(command, shell=True)
            return result
        except subprocess.CalledProcessError as error:
            tkinter.messagebox.showerror(
                "Erro ao executar o script",
                f"Ocorreu um erro ao executar o script: {error}\n"
                f"Saída do script:\n{error.stdout}"
            )
            return error

    @staticmethod
    def execButton(select):
        try:
            result = ControScript.execScript(select)
            return result
        except KeyError:
            tkinter.messagebox.showinfo("Informação", "Opção inválida selecionada!")
        except FileNotFoundError as error:
            tkinter.messagebox.showerror("Erro", str(error))

    @staticmethod
    def searchButton():
        dir_win = tkinter.filedialog.askopenfilename(title="Selecione um arquivo")

        if dir_win:
            options.append(dir_win)
            ControScript.execButton(dir_win)


        return dir_win