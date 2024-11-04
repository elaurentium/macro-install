import os
import json

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