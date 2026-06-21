arr=[1,2,3,4,5]
for i in range(len(arr)-1):
    if arr[i>arr[i-1]]:
        print("The array is not sorted in ascending order")
        break
else:    print("The array is sorted in ascending order")  