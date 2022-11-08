"""
JSON UTILS BY SUPERLEGO
"""
import json
def write(what,where):
    what=what
    clear(where)
    with open(where, "w") as write_file:
        json.dump(what, write_file)
    return True
def clear(what):
    with open(what,'w') as cleared:cleared.close()
    return True
def read(read):
    '''returns data'''
    try:
        with open(read, "r") as read_file:
            data = json.load(read_file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError("your data file does not exist.")