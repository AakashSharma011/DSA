arr=[1,1,0,1,1,1,0,0,1,1]
maxi=0
count=0
for i in range(len(arr)):
    if arr[i]==1:
        count+=1
        maxi=max(count,maxi)
    else:
        count=0
print("The maximum number of consecutive 1's is:", maxi)