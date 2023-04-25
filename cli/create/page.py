from os import system 
from os import path 
import os
import create.razor as razor

def generate(path, name, wrapped_name, **kwargs):
    reg_path = \
        f"app/{'/'.join(path) + '/' if path else ''}"+\
        f"{wrapped_name}"+\
        f"/{'(index)/' if kwargs['index'] else ''}"
    os.makedirs(reg_path, exist_ok=True)
    variants = {"default": True,**kwargs}
    args = {"page_name": name }
    from_path = "cli/create/page/" 
    pages = {
        "page.tsx": True, 
        "loading.tsx": True,
        "page.types.ts": True,
        "style.module.css": kwargs["styles"],
        "layout.tsx": kwargs["layout"],
        "error.tsx": kwargs["error"]
    }
    for p in pages:
        if pages[p]: razor.create_from(reg_path+p,from_path + p,variants, **args)

def page(*params):
    if not params: 
        print('''
create page <name> -flag: 
name - name of the page
flags:
\t-d - dynamic route
\t-a - catch-all route
\t-A - optional catch-all route
\t-g - group route
\t-i - put everything inside (index) folder
\t-e - generate error page
\t-l - generate layout file
\t-s - do not generate style file
\t-f - add fetch
        ''')
        return
    pathname = [i for i in params if i[0] != "-"][0]
    pathname = pathname.split("/")
    flags = ""
    for i in [i[1:] for i in params if i[0] == "-"]:
        flags += i 
    name = pathname[-1]
    path = pathname[:-1]
    describe = "regular"
    wrapped_name = name 
    if "d" in flags:
        wrapped_name = f"[{name}]"
        describe = "dynamic" 
    if "a" in flags:
        wrapped_name = f"[...{name}]"
        describe = "catch-all"
    if "A" in flags:
        wrapped_name = f"[[...{name}]]"
        describe = "optional catch-all"
    if "g" in flags:
        wrapped_name = f"({name})"
    
    print()
    print(f"Creating {describe} page: {name}")
    print(f"{'/'.join(path)}/{wrapped_name}/{'(index)' if 'i' in flags else ''}")
    if "g" in flags:
        print("│")
        if not "s" in flags: print("├─" + "style.module.css")
        print("└─" + "layout.tsx")
        if "e" in flags: print("Warning: no error pages in route group")
        if "t" in flags: print("Warning: no tests in route group")
        return 
    print("│")
    if "l" in flags: print("├─" + "layout.tsx")
    if "e" in flags: print("├─" + "error.tsx")
    if not "s" in flags: print("├─" + "style.module.css")
    print("├─" + "loading.tsx")
    print("├─" + "page.tsx")
    print("└─" + "page.types.ts")

    generate(path, name, wrapped_name, index="i" in flags, error="e" in flags, dynamic="d" in flags, styles=not "s" in flags, layout="l" in flags, fetch="f" in flags)
    
