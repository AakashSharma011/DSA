arr=[4,5,6,71,2]
low=0
high=len(arr)-1
ans=float('inf')
while low<=high:
    mid=low+(high-low)//2
    if arr[low]<=arr[mid]:
        ans=min(ans,arr[low])
        low=mid+1
    else:
        ans=min(ans,arr[mid])
        high=mid-1
print(ans)