arr=[1, 2, 3, 4, 5]
num =2
for i in range(len(arr)):
    if arr[i]==num:
        print("element found at index",i)
        break
else:
    print("element not found")