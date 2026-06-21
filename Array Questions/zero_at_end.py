arr=[1,2,0,3,4,0,4,0,2]
j=-1
for i in range(len(arr)):
    if arr[i]==0:
        j=i
        break
for i in range(j+1,len(arr)):
    if arr[i]!=0:
        arr[j],arr[i]=arr[i],arr[j]
        j+=1
print(arr)