import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mbox
from threading import Thread
import tasks

def _change(og,new,typeof):
    try:
        if type(typeof(new))==typeof:
            return typeof(new)
    except:pass
    return og

class Gui(tk.Tk):
    def loadFields(self):
        #self.goldvar.set(self.saoC.gold)
        #self.levelvar.set(self.saoC.level)
        self.taskvar.set(self.saoC.task)
        #self.guildvar.set(self.saoC.guild)
    def statusUpdate(self):
        #try:
        _=_change(self.saoC.task,self.taskvar.get(),str)
        self.saoC.task=_
        
        self.loadFields()
        
        _=_change(self.saoC.guild,self.guildvar.get(),str)
        self.guildvar.set("")
        if _!="":self.saoC.joinGuild(_)
        
        
        print(">> Interface updated status.")
        #except:print(">> Interface unable to update.")
    def loop(self): #logic loop
        pass
    def __init__(self,saoClient): #tk init
        while 1:
            super().__init__()
            #tk init
            self.lower()
            self.geometry("250x130+15+15")
            self.title("SAOClient")
            self.resizable(False,False)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=1)
            self.attributes('-alpha',0.9)
            #self.iconbitmap('./icon.ico')

            _=tk.Label(self,text="Task:")
            _.grid(row=0,column=0,pady=5)
            self.taskvar=tk.StringVar()
            _=ttk.Combobox(self,textvariable=self.taskvar)
            _['values']=tasks.names
            _.current(0)
            _['state']="readonly"
            _.grid(row=0,column=1,pady=5,sticky=tk.W)

            _=tk.Label(self,text="Guild:")
            _.grid(row=1,column=0,pady=5)
            self.guildvar=tk.StringVar()
            _=tk.Entry(self,textvariable=self.guildvar)
            _.grid(row=1,column=1,pady=5,sticky=tk.W)

            _=tk.Button(self,text="update",command=self.statusUpdate)
            _.grid(row=2,column=0,columnspan=2,pady=5)
            del _
    #:      #entries setup


            #var inint
            self.saoC=saoClient
            self.statusUpdate()


            #Thread(target=self.loop).start() #logic loop
            print("> Interface started.")
            self.lift()
            self.mainloop() #tk loop
            print(">>> what the hell stop closing the gui")
