tasks=[
    #[name,[riskmin,riskmax],[timemin,timemax],[healthmin,healthmax],[energymin,energymax],[levelmin,levelmax],[goldmin,goldmax]]
    ["AFK",0,-1,[-5,-10],[-5,-10],0,0],
    ["Questing",[5,20],[30,70],[10,30],[20,40],0,0],
    ["Grinding",[0,5],0,-5,[5,10],0,0],
    ["Sleeping",0.00001,[5*60,-1],[-80,-100],-100,0,0],
]
names=[]
for _,task in enumerate(tasks):
    names.append(task[0])