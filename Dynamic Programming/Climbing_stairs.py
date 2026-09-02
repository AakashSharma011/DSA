n=4
class Solution(object):

    def climbStairs(self, n):

        dp = {}

        def solve(i):

            if i == n:
                return 1

            if i > n:
                return 0

            if i in dp:
                return dp[i]

            dp[i] = solve(i + 1) + solve(i + 2)

            return dp[i]

        return solve(0)
print(Solution().climbStairs(n))