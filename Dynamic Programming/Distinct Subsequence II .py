s="abc"
class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        
        dp = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')
            
            total = sum(dp) % MOD
            
            dp[i] = total + 1
        
        return sum(dp) % MOD
print(Solution().distinctSubseqII(s))