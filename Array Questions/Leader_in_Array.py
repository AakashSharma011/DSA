arr = [1, 2, 3, 2]

ans = []
mx = 0

for x in arr[::-1]:
    if x > mx:
        ans.append(x)
        mx = x

print(ans[::-1])