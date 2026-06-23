arr = [5, 8, 3, 2, 1, 4]

st = set(arr)
longest = 0

for num in st:

    # sequence ka starting point hai ya nahi
    if num - 1 not in st:

        cnt = 1
        x = num

        while x + 1 in st:
            x += 1
            cnt += 1

        longest = max(longest, cnt)

print(longest)