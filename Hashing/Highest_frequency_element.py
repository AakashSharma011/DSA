arr = [1,2,1,3,2,1]

freq = {}

for x in arr:
    freq[x] = freq.get(x,0)+1

max_freq = 0
ans = -1

for key,val in freq.items():
    if val > max_freq:
        max_freq = val
        ans = key

print(ans)