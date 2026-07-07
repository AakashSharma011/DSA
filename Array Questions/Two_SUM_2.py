arr=[1,2,2,4,7,5,3,6]
target=9
hash_map = {}
def two_sum(arr, target):
    for i in range(len(arr)):
        diff=target - arr[i]
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[arr[i]] = i
result = two_sum(arr, target)
print(result)
