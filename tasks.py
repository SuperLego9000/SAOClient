tasks=[
    #[name,[riskmin,riskmax],[timemin,timemax],[healthmin,healthmax],[energymin,energymax],[levelmin,levelmax],[goldmin,goldmax]]
    ["AFK",0,0,[-5,-10],[-5,-10],0,0],
    ["Questing",[5,20],[30,70],[10,30],[20,40],[1,4],[70,130]],
    ["Grinding"],
    ["Sleeping"],
]
names=[]
for _,task in enumerate(tasks):
    names.append(task[0])