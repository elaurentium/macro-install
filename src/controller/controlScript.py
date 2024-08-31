import subprocess
import tkinter
import tkinter.messagebox
from pathlib import Path

def execScript(scriptPath):
    script_path = Path(scriptPath)

    if not script_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {script_path}")
    
    command = ["powershell", "-NoExit", "-Command", f"Start-Process powershell -ArgumentList '-NoExit', '-File', '{script_path}'"]

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


def execButton(select):
    script_paths = {
        "Script Completo": r"C:\Users\evandro.limeira\Documents\macro.ps1",
        "Atualização": r"W:\Programas\DB\atualizar.ps1",
        "XPTO": r"C:\Users\meu_script_xpto.ps1"
    }

    try:
        script_path = script_paths[select]
        result = execScript(script_path)

        return result
    except KeyError:
        tkinter.messagebox.showinfo("Informação", "Opção inválida selecionada!")
    except FileNotFoundError as error:
        tkinter.messagebox.showerror("Erro", str(error))