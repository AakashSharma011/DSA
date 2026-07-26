n=11
def hammingWeight(self, n):
        res=0
        while n>0:
            res+=1
            n=  n & n-1
        return res
print(hammingWeight(0,n))