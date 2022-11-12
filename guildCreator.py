import FileUtils as flu
import Encrypt as enc
from os import system as sys
sys("title guildCreator")
sys("cls")
while 1:
    try:
        print()
        name=input("Server Name: ")
        join=input("Discord server Invite: ")
        save=input("join server? (Y) : ")
        save = True if save=="Y" else False
        join=join.split("\\")[-1]

        raw=enc.encode([name,join])
        if save:print("saving server...");flu.write(".guild", raw)

        print(f"key: {raw}")
        print(enc.decode(raw))
    except:print("\nan error occured.\n")