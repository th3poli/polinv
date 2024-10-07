import os
import json

def read(path: str, mode: str = 'r'):
    if not os.path.isfile(path): return
    encoding = None if mode == 'rb' else 'utf-8'
    with open(path, mode, encoding=encoding) as file: return file.read()

def readJSON(path: str):
    if not os.path.isfile(path): return
    with open(path, 'r', encoding='utf-8') as file: return json.load(file)

def write(path: str, data: str, mode: str = 'w'):
    encoding = None if mode == 'wb' else 'utf-8'
    with open(path, mode, encoding=encoding) as file: return file.write(data)

def writeJSON(path: str, data: dict):
    with open(path, 'r', encoding='utf-8') as file: return json.dump(data, file)

def join(path: str, *paths: str): return os.path.join(path, *paths)
def join_and_make(path: str, *paths: str): return makedirs(join(path, *paths))

def exists(path: str): return os.path.exists(path)
def makedirs(path: str, mode: int = 511, exist_ok: bool = True): return os.makedirs(path, mode, exist_ok)
