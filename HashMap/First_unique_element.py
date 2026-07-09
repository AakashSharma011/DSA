s='leetcode'
n= len(s)
hash_map = {}
def first_unique(s):
    for i in range(n):
        if s[i] in hash_map:
            hash_map[s[i]] += 1
        else:
            hash_map[s[i]] = 1
    for i in range(n):
        if hash_map[s[i]] == 1:
            return i
    return -1
result = first_unique(s)
print(result)   