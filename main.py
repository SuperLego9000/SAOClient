from os import system as sys
sys("title SAOClient Console")
sys("color 0e")

print("Minimize this tab.\n")
del sys



#bad file verify
import JsonUtils as jsu
#f=open("data.sao","w+") 
#if f.read()=="":f.write('{ }')
#f.close()
#del f
import interface
import secrets_app
import guildParser
import webbrowser
import pypresence as pyp
from time import sleep as wait
from threading import Thread
from os import remove as rm
from datetime import datetime
from random import randint

def _getYearDay():
    return int(datetime.now().timetuple().tm_yday)

class sao():
    health=100
    energy=100
    gold=0
    level=1
    task=""
    timestamp=0
    guild=""
    day=1
    
    auto=False
    yearday=-1
    
    def awaitGuild(self):
        """
        awaits ".guild" file in cd and joins guild and deletes file
        holds execution
        """
        print("> listening for guilds...")
        while 1:
            wait(5)
            try:
                with open(".guild","r") as f:
                    key=f.readline()
                    
                print(">> joining guild from link")
                print(">>> "+key)
                self.joinGuild(key)
                rm(".guild")
            except FileNotFoundError:pass
            except:print("listener died lol")
    def joinGuild(self,key):
        print("> joining guild...")
        #key="WyJ0aGUgam9lcyIsIkFXRkFXRkdXIl0="
        try:
            [name,invite]=guildParser.convert(key)
            url="https://discord.gg/"+invite
            webbrowser.open_new(url)
            self.guild=name
            print(">> guild joined successfully.")
            print(">>> "+self.guild)
            print(">>> "+url)
        except:print("> failed to join guild.")
    def autoStats(self):
        """
        auto increment level and gold
        holds execution
        """
        print("> autoProgress starting... ")
        while 1:
            if self.auto:print("> autoProgress started.")
            while self.auto:
                dura=randint(15,60)
                print(f">> stats update in {dura} minutes")
                for c in range(dura*randint(58,60)):
                    if not self.auto:print(">> autoProgress cancelled.");break
                    wait(1)
                if not self.auto:break #if we swapped to off during wait
                print(">> autoProgress assigning...")
                # random complexe algorithms for stats
                self.level+=int((randint(1,2)/2)*((dura/(randint(1200,2400)/10))*2))
                self.gold+=int((randint(1,2)/2)*((dura/(randint(30,35)/10))*2))
                print(">>> autoProgress updated. ")
            wait(3)
    
    def dayCounter(self):
        """
        auto increment day count
        holds execution
        """
        print("> listening for day change...")
        self.yearday=_getYearDay()
        while 1:
            wait(30)
            if _getYearDay()!=self.yearday:
                self.yearday=_getYearDay()
                self.day+=1
                print(f">> new day, {self.day}")
                wait(0)
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
            f"""{"In Guild '"+self.guild+"'" if self.guild else "Empty Party"}""",
            None if self.timestamp==0 else self.timestamp
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
        print("> hooking Discord...")
        self.appid=appid
        self.Client=pyp.Presence(self.appid)
        self.Client.connect()
        self.saoC=saoClient
        print(">> Client started.")
    def loop(self):
        """
        begin handshake
        holds execution
        """
        print(">> Discord hooked.")
        while 1:
            print(">>  refreshing status...")
            (self.details,self.state,start)=self.saoC.get()
            self.Client.update(large_image="sao",large_text="Sword Art Online",
                details=self.details,
                state=self.state,
            )
            self.saoC.save()
            wait(15)


mysao=sao()
myp=pwrite(appid=secrets_app.appid,saoClient=mysao)
Thread(target=myp.loop).start()
#Thread(target=mysao.loop).start()
Thread(target=mysao.awaitGuild).start()
Thread(target=mysao.dayCounter).start()
Thread(target=mysao.autoStats).start()
mygui=interface.Gui(mysao) #holds main thread just because