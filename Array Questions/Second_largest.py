arr=[1,43,55,45,45,55,64,24,64,62]
largest=arr[0]
second_largest=-1
for i in arr:
    if i> largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i !=largest:
        second_largest=i
    
print("The second largest element in the array is:", second_largest)    