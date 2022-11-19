from os import system
from os import chdir
system("title sao uri handler")
import sys
from time import sleep as wait
import FileUtils as flu
import Encrypt as enc
from subprocess import call as execute
args=sys.argv
print(args)
#args=['C:\\Program Files\\sao\\uri.exe','sao:///?joinguild:WyJ0aGUgam9lcyIsIkFXRkFXRkdXIl0=']
#args=[path,full_Uri]
path=args[0].split(":")[0]
path=path+":\\Program Files\\sao\\"
print(path+".guild")
chdir(path)
#wait(9e3)

def getDesire(rawArg:str=None):
    try:
        trimmed=rawArg.split(r"sao:///")[1]
        desire=None
        desire = 1 if trimmed.startswith("?joinguild:") else desire
        # more settings here
        return desire
    except:return None

if 1:
    desire=getDesire(args[1])
    if desire==1:
        guild=str(args[1].split(":")[-1])
        flu.write(".guild",guild)
        print("guild request sent.")  
        print(guild)  
    else:
        print("invalid uri scheme.")
print("waiting...")
wait(5)

#except:print("oh crap somhti hapen")