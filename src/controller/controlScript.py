import subprocess
import os
import tkinter
import tkinter.messagebox
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env.local')

server = os.getenv('HD_CLOUD_SERVER')

def execScript(scriptPath):
    script_path = Path(scriptPath)

    if not script_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {script_path}")
    
    command = f'cmd /c start cmd /k "{script_path}"'
    
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
        "Script Completo": rf"\\{server}\Info_Fabrica\Informatica e Telecom\Suporte - Infra\___BASE INSTALL\ALLINSTALL.cmd",
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