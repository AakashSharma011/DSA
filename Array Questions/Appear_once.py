arr=[1,1,2,3,3,4,4]
Xor=0
for i in range(len(arr)):
    Xor=Xor^arr[i]
print("The number that appears only once is:",Xor)