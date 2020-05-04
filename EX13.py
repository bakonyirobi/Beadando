import random
def random_two(n):
    f=open("output.txt", 'w')
    n = int(n)
    teams=[]
    rndteams=[]
    for i in range(n):
        teams.append(i+1)
    print("csapatok:")
    print(teams)
    for j in range(0,n,2):
        rndteams.append(random.randint(teams[j],teams[j+1]))
    print("tovabbjutok:")
    print(rndteams)
    print("|--------------------|")
    print("Team"+str(teams[0])+"--->|",file=f)
    print("\t","\t","-|Team"+str(rndteams[0])+"|-",file=f)
    print("Team"+str(teams[1])+"--->|",file=f)
    f.close()

def random_four(n):
    f = open("output.txt", 'w')
    n = int(n)
    teams=[]
    rndteams=[]
    for i in range(n):
        teams.append(i+1)
    print("csapatok:")
    print(teams)
    for j in range(0,n,2):
        rndteams.append(random.randint(teams[j],teams[j+1]))
    print("tovabbjutok:")
    print(rndteams)
    print("|--------------------|")
    print("Team"+str(teams[0])+"---",file=f)
    print("\t","\t"+"|Team"+str(rndteams[0])+"---",file=f)
    print("Team"+str(teams[1])+"---",file=f)
    print("\t","\t""\t","\t"+"|-Team"+str(random.randint(rndteams[0],rndteams[1]))+"-|",file=f)
    print("Team"+str(teams[2])+"---",file=f)
    print("\t","\t"+"|Team"+str(rndteams[1])+"---",file=f)
    print("Team"+str(teams[3])+"---",file=f)
    f.close()

n=int(input("Add meg a csapatok számát(2 hatványai lehetnek):"))
if n==2:
    random_two(n)
if n==4:
    random_four(n)