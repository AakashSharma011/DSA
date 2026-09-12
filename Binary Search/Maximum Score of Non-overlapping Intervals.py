intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]
class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        arr = []
        for i in range(n):
            start, end, weight = intervals[i]
            arr.append((end, start, weight, i))

        arr.sort()

        ends = [x[0] for x in arr]

        # dp[i][k] = best answer using first i intervals,
        # selecting at most k intervals
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            end, start, weight, idx = arr[i - 1]

            # Find last interval with end < start
            lo = 0
            hi = i - 2
            prev = -1

            while lo <= hi:
                mid = (lo + hi) // 2

                if ends[mid] < start:
                    prev = mid
                    lo = mid + 1
                else:
                    hi = mid - 1

            for k in range(1, 5):
                # Don't take current interval
                best = dp[i - 1][k]

                # Take current interval
                old_score, old_indices = dp[prev + 1][k - 1]
                take = (old_score + weight, old_indices + [idx])

                if take[0] > best[0]:
                    best = take
                elif take[0] == best[0]:
                    if sorted(take[1]) < sorted(best[1]):
                        best = take

                dp[i][k] = best

        return sorted(dp[n][4][1])
print(Solution().maximumWeight(intervals))