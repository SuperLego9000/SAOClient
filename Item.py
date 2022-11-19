class Item():
    """constructor for items"""
    count=1
    name="NUL"
    disc="NUL"
    health=0
    energy=0
    level=0
    stackSize=50
    value=0
    def _dump(self):
        print(
f"""item dump;
    {self.count}/{self.stackSize}
    {self.name}
    {self.disc}
    {self.health}
    {self.value}
""")
    def __init__(self,name:str="NUL",discription:str="NUL",count:int=1,health:int=0,energy:int=0,level:float=0,stackSize:int=50,value:int=0):
        self.name=name
        self.disc=discription
        self.health=health
        self.energy=energy
        self.level=level
        self.value=value
        self.count=count
        
class Database:
    def _toID(itemName):
        """returns id of item"""
        for a,catagory in enumerate(Database.catalog):
            for b,item in enumerate(catagory):
                if item.name==itemName:return a,b
    def _fromID(a,b):
        return Database.catalog[a][b]
    def fromName(name):
        return Database._fromID(*Database._toID(name)) or Item()
    catalog=[    
        [#food
            Item("Apple","yumyum nomnom",health=5),
            Item("Health Potion","sussy potion give health",health=20)
        ],
        [#quest items

        ],
        [#misc

        ]
    ]