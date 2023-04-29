from os import system

libs = {
    "tabler-icons-react":   ["icons", "Icons library"],
    "react-dnd":            ["dnd", "Drag and Drop library"],
    "react-cva":            ["cva", "Class value authority to manage styles"],
    "classnames":           ["cn", "Manage classes conditionally"],
    "react-motion":         ["motion", "Animations library"],
    "react-hook-form":      ["form", "Library to work with forms"]
}

install_libs = {}
for lib in libs:
    install_libs[lib] = lambda x=lib: system("npm i " + x)
    install_libs[libs[lib][0]] = lambda x=lib: system("npm i " + x)

remove_libs = {}
for lib in libs:
    remove_libs[lib] = lambda x=lib: system("npm uninstall " + x)
    remove_libs[libs[lib][0]] = lambda x=lib: system("npm uninstall " + x)
