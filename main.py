from os import system as sys
sys("title SAOClient")
print("Minimize this tab.\n")
del sys

#bad file verify
import JsonUtils as jsu
#f=open("data.sao","w+") 
#if f.read()=="":f.write('{ }')
#f.close()
#del f

import pypresence as pyp
from time import sleep as wait
from threading import Thread
class sao():
    gold=0
    level=1
    task=""
    guild=""
    day=1
    def load(self):
        try:
            save=jsu.read("data.sao")
            self.gold=save['gold']
            self.level=save['level']
            self.guild=save['guild']
            self.day=save['day']
            print(">>> data loaded.")
        except:print(">>> save missing or corrupted.")
    def __init__(self):
        self.load()
    def change(self,gold:int=None,level:int=None,task:str=None,guild:str=None,day:int=None):
        pass
    def get(self):
        return (
            f"Day {self.day} | Level {self.level} | Gold {self.gold}{f' | {self.task}' if not self.task=='' else ''}",
            f"""{"In Guild '"+self.guild+"'" if self.guild else "Empty Party"}"""
            )
    def save(self):
        save={
            "gold":self.gold,
            "level":self.level,
            "guild":self.guild,
            "day":self.day
        
        }
        jsu.write(save, "data.sao")
        print(">>> data saved.")


class pwrite:
    details=""
    state=""
    appid=None
    client=None
    saoC=None
    def __init__(self,appid,saoClient):
        self.appid=appid
        self.Client=pyp.Presence(self.appid)
        self.Client.connect()
        self.saoC=saoClient
        print("> Client started.")
    def loop(self):
        print("> Discord hooked.")
        while 1:
            print(">>  refreshing status...")
            (self.details,self.state)=self.saoC.get()
            self.Client.update(large_image="sao",large_text="Sword Art Online",
                details=self.details,
                state=self.state
            )
            self.saoC.save()
            wait(15)


myp=pwrite(appid=1038959788320636928,saoClient=sao())
Thread(target=myp.loop).start()
while 1:
    wait(60)
    #do logic