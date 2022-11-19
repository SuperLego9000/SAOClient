from time import sleep as wait
from Item import Item
class Inventory():
    slots=[4,4,{}]
    def trim(self):
        """deletes overflow items and unloads depleted items"""
        remove=[]
        for _,xy in enumerate(self.slots[2]):
            item=self.slots[2][xy]
            if item.count<= 0:
                print(f">>>> item depleted; {xy};{item.count}")
                remove.append(xy)
        for _,xy in enumerate(remove):
            del self.slots[2][xy]
    def get(self):
        """returns slots after trimming"""
        self.trim()
        return self.slots
    def getFromSlot(self,a,b):
        """returns iten from slot (a,b)"""
        self.trim()
        xy=f"{a},{b}"
        slot=False
        try:slot=self.slots[2][xy]
        except:print(">>>> slot empty")
        return slot
        pass
    def give(self,item:Item,count:int=1):
        """adds 'item' to inventory in nearest spot"""
        print(f">>> adding {count} {item.name}")
        item.count=1 # no cheating bozo
        self.trim()
        given=0
        while given<=count:
            if given>=count:break #we need this for some reason
            #print(given)
            wait(1/60)
            self.trim()
            slotswith=self._getSlotsFromName(item.name)
            if slotswith: #if we are adding to a stack
                for _,slot in enumerate(slotswith):
                    if given>=count:print("fs");break
                    if slot.count<slot.maxSize:
                        am=min(slot.maxSize,count-given)
                        slot.count+=am
                        given+=am
                        break
            else:
                given+=1
                if not self._getEmptySlot():print(">>> no empty slots");break
                self.slots[2][self._getEmptySlot()]=item
                    
    def _getEmptySlot(self):
        """returns empty slot"""
        self.trim()
        for x in range(self.slots[0]):
            x+=1
            for y in range(self.slots[1]):
                y+=1
                xy=f"{x},{y}"
                #print(xy)
                try:self.slots[2][xy] #haha try exploit
                except:return xy
        return False
    def _getSlotsFromName(self,name:str=""):
        """returns slots containing item named 'name' or returns false if no item"""
        slots=[]
        for _,xy in enumerate(self.slots[2]):
            item=self.slots[2][xy]
            if item.name==name:slots.append(item)
        return slots if slots!=[] else False
    def _remove(self,a,b,r):
        """removes item at x,y and returns removed ammount"""
        xy=f"{a},{b}"
        self.trim()
        slot=self.slots[2][xy]
        c=min(r,slot.count)
        self.slots[2][xy].count-=c
        self.trim()
        #del self.slots[2][xy]
        print(f">>>> removed item at slot {xy}")
        pass
    def use(self,a,b,r):
        """removes 'r' items at 'a','b' and applies effects 'r' times"""
        self.trim()
        print(f">>> using item at {a,b}...")
        item=self.getFromSlot(a,b)
        if not item:print(f">>>> failed to use item 'NUL' at {a,b}");return False
        #print(dir(item))
        #print(item.name)
        r=min(r,item.count)
        #item in slot
        print(f">>>> using '{item.name}' {r} times")
        item._dump()
        for c in range(int(r)):
            self.saoC.health+=item.health
            self.saoC.energy+=item.energy
            self.saoC.level+=item.level
        self._remove(a,b,r)
        self.saoC.statNormalize()
        pass
    def sell(self,a,b,r):
        "removes 'r' items at 'a','b' and adds cash value * 'r'"
        pass
    def __init__(self,saoClient=None):
        self.saoC=saoClient
        
if __name__=="__main__" and False:
    
    from Item import database as catalog
    inv=Inventory()
    print(inv.get())
    inv.use(1,1,5)
    #inv.give(catalog[0][1])
    print(inv.get())