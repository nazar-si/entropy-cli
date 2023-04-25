from os import system 
from os import path 
import os
from libs import libs, remove_libs, install_libs 
from copy_func import copy_func
from sys import argv

from create.page import page

path = "\\".join(path.realpath(__file__).split("\\")[:-2])
os.chdir(path)

commands_help = {
    "clear":    "Clears all previous console outputs",
    "create":   "Create new object inside project",
    "cd": "Set current working directory",
    "help":     "Get all commands list",
    "install":  "Install and configure new libraries",
}

context = []
cd = ""

def change_dir(*params):
    global cd
    cd = params[0]

clear = lambda: system("cls")
back = lambda: context.pop()
base = {
    "clear": clear,
    "..": back
}


commands = {
    "help": lambda: print("\n".join([f'{k}: {v}' for k, v in commands_help.items()])),
    "clear": clear,
    "cd": change_dir,
    "create": {
        **base,
        "page": page,
    },
    "install": {
        **base,
        "help": lambda: print("\n".join([f'{k} ({v[0]}): {v[1]}' for k, v in libs.items()]) + "\n\n Print 'install (short-name)/name' to install"),
        **install_libs
    },
    "remove": {
        **base,
        "help": lambda: print("\n".join([f'{k} ({v[0]}): {v[1]}' for k, v in libs.items()]) + "\n\n Print 'remove (short-name)/name' to remove"),
        **remove_libs
    },
}

aliases = {
    "c":    "create",
    "i":    "install",
    "r":    "remove",
    "cls":  "clear",
    "h":    "help",
    "p":    "page"
}
def query(q):
    global context 
    arr = context + q.strip().split(" ")
    com = commands
    params = []
    num = 0
    for i, a in enumerate(arr):
        num = i
        if a[0] == "-" or callable(com):
            params = arr[num:]
            break 
        if not a in com and not (a in aliases and aliases[a] in com):
            print("Unknown command:", " ".join(arr[:i + 1]))
            return 
        if a in com: 
            com = com[a]
            continue 
        com = com[aliases[a]]
    if not callable(com):
        context = context + arr[:num + 1]
        return 
    try:
        com(*params)
    except TypeError:
        print("Wrong arguments")

if len(argv) > 1:
    a = " ".join(argv[1:])
    query(a)
    exit()

while True:
    a = input("/".join(context) + ">>")
    if a == "exit":
        break 
    query(a)
