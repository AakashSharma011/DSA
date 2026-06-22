arr=[1,2,2,4,7,5,3,6]
target=9

sorted_arr=sorted(arr)
left=0
right=len(sorted_arr)-1
while left<right:
    if sorted_arr[left]+sorted_arr[right]==target:
        print("The two numbers that add up to the target are:", sorted_arr[left], "and", sorted_arr[right])
        break
    elif sorted_arr[left]+sorted_arr[right]<target:
        left+=1
    else:
        right-=1   