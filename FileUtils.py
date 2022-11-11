"""simple module to write files pythonicly"""
def read(file):
    with open(file,"r") as f:
        return f.read()
def write(file,data:str):
    with open(file,"w") as f:
        f.write(data)