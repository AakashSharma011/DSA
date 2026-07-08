s="abccccdd"

def longestPalindrome(self, s):
        hashmap = {}

        # Frequency count
        for ch in s:
            if ch in hashmap:
                hashmap[ch] += 1
            else:
                hashmap[ch] = 1

        ans = 0
        has_odd = False

        for freq in hashmap.values():
            if freq % 2 == 0:
                ans += freq
            else:
                ans += freq - 1
                has_odd = True

        if has_odd:
            ans += 1

        return ans
print(longestPalindrome(0, s))
    