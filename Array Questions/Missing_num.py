# Sum solution
arr=[1,2,4,5]
Xor1=0
Xor2=0
N=len(arr)+1
for i in range(N-1):
    Xor2=Xor2^arr[i]
    Xor1=Xor1^(i+1)
Xor1=Xor1^N
    

print("The missing number is:",Xor1^Xor2)