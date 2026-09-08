n = 1002
class Solution:
    def countCommas(self, n):
        ans = 0

        if n >= 1000:
            ans += n - 999

        if n >= 1000000:
            ans += n - 999999

        return ans
print(Solution().countCommas(n))