s = "aabacbebebe"

def longest_substring_k_unique(s, k):
    left = 0
    max_len = 0
    freq = {}

    for right in range(len(s)):
        if s[right] in freq:
            freq[s[right]] += 1
        else:
            freq[s[right]] = 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        if len(freq) == k:
            max_len = max(max_len, right - left + 1)

    return max_len

print(longest_substring_k_unique(s, 3))