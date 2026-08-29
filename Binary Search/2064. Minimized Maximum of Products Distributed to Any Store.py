n = 6
quantities = [11,6]
class Solution(object):
    def minimizedMaximum(self, n, quantities):
        def check(max_products):
            num = 0

            for x in quantities:
                num += (x + max_products - 1) // max_products

            return num <= n
        low = 1
        high = max(quantities)

        while low <= high:

            mid = low + (high - low) // 2

            if check(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low

print(Solution().minimizedMaximum(n,quantities))