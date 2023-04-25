import re 
import typing

def read_sections(path: str, select: typing.Dict, **kwargs):
    ref = open(path, "r")
    raw_data =ref.read()
    for arg in kwargs:
        raw_data = raw_data.replace('{{' + arg + '}}', kwargs[arg])

    match = re.findall(r"//\((?:\w|\-|\!)*\)\{(?:.|\n)*?//\}", raw_data)
    match_groups = {}
    for m in match:
        name = m[3:m.find(")")]
        if name not in match_groups:
            match_groups[name] = [m]
        else:
            match_groups[name].append(m)
    for s in select:
        if s in match_groups and not select[s]:
            for string in match_groups[s]:
                raw_data = raw_data.replace(f"{string}\n", "")
        elif s in match_groups:
            for string in match_groups[s]:
                raw_data = raw_data.replace(f"{string}\n", string[string.find("{") + 2: string.rfind("//")]) 
        if f"!{s}" in match_groups and select[s]:
            for string in match_groups[f"!{s}"]:
                raw_data = raw_data.replace(f"{string}\n", "")
        elif f"!{s}" in match_groups:
            for string in match_groups[f"!{s}"]:
                raw_data = raw_data.replace(f"{string}\n", string[string.find("{") + 2: string.rfind("//")]) 
    
    data = raw_data.split("//:")

    sections = []
    for d in data:
        if len(d) <= 1:
            continue
        name = d[:d.find("\n")]
        if name.replace(" ", "") == "":
            name = "default"
        if not name in select or (name in select and not select[name]):
            if not(name[0] == "!" and name[1:] in select and not select[name[1:]]):
                continue 
        sections.append(d[d.find("\n")+1:])
    ref.close()
    return "\n".join(sections) 

def create_from(path, read_path, sections, **kwargs):

    s = read_sections(read_path, sections, **kwargs)
    with open(path, "w+") as ref:
        ref.write(s)
