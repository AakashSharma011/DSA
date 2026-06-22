arr=[2, 2, 1, 1, 1, 2, 2]
cnt=0
el=arr[0]
for i in range(len(arr)):
    if cnt==0:
        cnt=1
        el=arr[i]
    elif arr[i]==el:
        cnt+=1
    else:   
         cnt-=1

# Verification
cnt=0
for num in arr:
    if num==el:
        cnt+=1

if cnt > len(arr)//2:
    print("The majority element is:", el)
else:
    print("There is no majority element in the array.")
