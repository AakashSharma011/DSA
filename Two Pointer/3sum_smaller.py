arr=[-2,3,43,23,0,13,2]
arr.sort()
target=10
def threeSumSmaller(arr,target):
    ans=0
    for i in range(len(arr)-2):
        left=i+1
        right=len(arr)-1
        while left<right:
            total=arr[i]+arr[left]+arr[right]
            if total>=target:
                right-=1
            else:
                ans=ans+(right-left)
                left+=1
    return ans
print(threeSumSmaller(arr,target))