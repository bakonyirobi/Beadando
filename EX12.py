#inputstr="34545488"
def alternalo(inputstr):
    inputstrlst=[]
    print(inputstr)
    paros=['0','2','4','6','8']
    paratlan=['1','3','5','7','9']
    checklist=[]
    alternal=[]
    alternal2=[]
    for l in inputstr:
        inputstrlst.append(l)
    for i in inputstr:
        if i in paros:
            checklist.append("paros")
        if i in paratlan:
            checklist.append("paratlan")
    for j in range(0,len(checklist)-1,2):
        if checklist[j]=="paros" and checklist[j+1]=="paratlan":
            alternal.append(inputstrlst[j])
            alternal.append(inputstrlst[j+1])
        else:
            break
    for k in range(0,len(checklist)-1,2):
        if checklist[k]=="paratlan" and checklist[k+1]=="paros":
            alternal2.append(inputstrlst[k])
            alternal2.append(inputstrlst[k+1])
        else:
            break
    if len(alternal) > len(alternal2):
        return alternal
    if len(alternal) < len(alternal2):
        return alternal2
inputstr=input("Adj meg egy sorozatot:")
print(alternalo(inputstr))
#print(inputstrlst)
#print(checklist)
#print(alternal)
#print(alternal2)