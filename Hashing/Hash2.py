s = input()

# Precompute
hash_arr = [0] * 26

for ch in s:
    hash_arr[ord(ch) - ord('a')] += 1

q = int(input())

while q > 0:
    c = input().strip()

    if len(c) != 1:
        print("Please enter a single character")
    else:
        print(hash_arr[ord(c) - ord('a')])

    q -= 1