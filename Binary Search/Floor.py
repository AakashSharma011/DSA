arr=[1,2,3,4,5,6,7,8,9,10]
low=0
high=len(arr)-1
x=5
answer=-1

while low<=high:
    mid=low+(high-low)//2
    if arr[mid]<=x:
        answer=mid
        low=mid+1
    else:
        high=mid-1

print("Floor of", x, "is at index", answer)