numbers = [2,7,11,15]
target = 9
def twoSum(self, numbers, target):
        left=0
        n=len(numbers)
        right=n-1
        while left < right :
            total=numbers[left]+numbers[right]
            if total == target:
                return [left+1,right+1]
            elif total>target:
                right-=1
            else:
                left+=1
print(twoSum(0, numbers, target))