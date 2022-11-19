from os import system as sys
sys("title SAOClient Console")
sys("color 0e")

print("Minimize this tab.\n")
del sys




#import JsonUtils as jsu
from json import dumps as jsonDumps
from json import loads as jsonLoads
import FileUtils as flu
import interface
import secrets_app
import Encrypt
import webbrowser
import pypresence as pyp
import Inventory
from time import sleep as wait
from threading import Thread
from os import remove as rm
from datetime import datetime
from random import randint

def _getYearDay():
    return int(datetime.now().timetuple().tm_yday)
def _forceRange(low,val,high):
    """ensures val is inbetween low and high"""
    val=min(high,val)
    val= max(low,val)
    return val

class sao():
    health=100
    energy=100
    hunger=100 #unimplemented
    gold=0
    level=1
    task=""
    timestamp=0
    guild=""
    day=1
    
    auto=False
    yearday=-1
    
    slots=[4,4]
    inventory=None
    
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
            [name,invite]=Encrypt.decode(key)
            for _,check in enumerate([name,invite]): #no cheating bozo
                bad=False
                for _,badchar in enumerate(["'",'"',"]","[",","]):
                    if badchar in check:bad=True
                    if bad:break
                if bad:
                    print(">>>stupid cheater")
                    crash() #will fail try
                    if False:
                        rm("sao.data")
                        self.load()


            url="https://discord.gg/"+invite
            webbrowser.open_new(url)
            self.guild=name
            print(">> guild joined successfully.")
            print(">>> "+self.guild)
            print(">>> "+url)
        except:print("> failed to join guild.")
    def statNormalize(self):
        self.health=_forceRange(0,self.health,100)
        self.energy=_forceRange(0,self.energy,100)
        self.level=_forceRange(0,self.level,100)
        #self.gold=_forceRange(,self.gold,)
        self.day=_forceRange(1,self.day,self.day+1)
        self.timestamp=_forceRange(0,self.timestamp,self.timestamp+1)
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
                #time for taxes hehehe
                print(">>> the government takes taxes")
                self.gold-=0 #consult how to handle taxes
                
    def load(self):
        try:
            save=flu.read("data.sao")
            save=Encrypt.decode(save)
            save=jsonLoads(save)
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
        save=jsonDumps(save)
        save=Encrypt.encode(save)
        flu.write("data.sao", save)
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

if __name__=="__main__":
    threads=[]
    mysao=sao()
    myp=pwrite(appid=secrets_app.appid,saoClient=mysao)
    threads.append(Thread(target=myp.loop))
    #Thread(target=mysao.loop).start()
    threads.append(Thread(target=mysao.awaitGuild))
    threads.append(Thread(target=mysao.dayCounter))
    threads.append(Thread(target=mysao.autoStats))
    mysao.inventory=Inventory.Inventory(mysao)
    for _,thread in enumerate(threads):thread.start()#;wait(0.25)
    
    if True: #inventory test
        wait(1)
        print("inventory test!")
        from Item import Database
        mysao.health=10
        mysao.inventory.give(Database.fromName("Apple"))
        mysao.inventory.use(1,1,5)
        print(mysao.health)
        print("end test.\n")
    
    mygui=interface.Gui(mysao) #holds main thread just because