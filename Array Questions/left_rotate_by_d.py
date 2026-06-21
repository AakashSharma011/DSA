"""arr=[1,2,3,4,5,6,7,8,9]
d=2
temp=arr[:d]
for i in range(d,len(arr)):
    arr[i-d]=arr[i]
arr[len(arr)-d:]=temp
print(arr)"""

# More optimized way to left rotate an array by d elements
arr=[1,2,3,4,5,6,7,8,9]
d = 3

arr[:d] = reversed(arr[:d])
arr[d:] = reversed(arr[d:])
arr.reverse()

print(arr)