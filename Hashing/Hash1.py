arr = [1,2,1,2,3,4,1,6]
freq = {}

k = int(input("Enter the number to find frequency: "))

def num(arr, k):
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1

    return freq.get(k, 0)

print(num(arr, k))