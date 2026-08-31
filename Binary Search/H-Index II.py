citations = [0,1,3,5,6]
class Solution:
    def hIndex(self, citations):
        n = len(citations)

        low = 0
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2

            if citations[mid] >= n - mid:
                high = mid - 1
            else:
                low = mid + 1

        return n - low
print(Solution().hIndex(citations))