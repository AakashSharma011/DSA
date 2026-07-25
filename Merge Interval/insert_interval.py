class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        inserted = False

        # Step 1: Correct position par insert karo
        for interval in intervals:

            if not inserted and newInterval[0] <= interval[0]:
                res.append(newInterval)
                inserted = True

            res.append(interval)

        # Agar sabse end me insert hona tha
        if not inserted:
            res.append(newInterval)

        # Step 2: Merge Intervals (LeetCode 56)
        ans = []

        start = res[0][0]
        end = res[0][1]

        for i in range(1, len(res)):
            start2 = res[i][0]
            end2 = res[i][1]

            if end >= start2:
                end = max(end, end2)
            else:
                ans.append([start, end])
                start = start2
                end = end2

        ans.append([start, end])

        return ans