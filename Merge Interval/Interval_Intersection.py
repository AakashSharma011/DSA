firstList = [[0,2],[5,10],[13,23],[24,25]] 
secondList = [[1,5],[8,12],[15,24],[25,26]]
def intervalIntersection(self, firstList, secondList):
    res=[]
    i=0
    j=0
    while i<len(firstList) and j<len(secondList):
        if max(firstList[i][0],secondList[j][0])<=min(firstList[i][1],secondList[j][1]):
            s1=max(firstList[i][0],secondList[j][0])
            e1=min(firstList[i][1],secondList[j][1])
            res.append([s1,e1])

        if firstList[i][1]>secondList[j][1]:
            j+=1
        else:
            i+=1
    return res
print(intervalIntersection(0,firstList,secondList))