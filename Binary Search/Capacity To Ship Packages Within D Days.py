weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
class Solution(object):
    def shipWithinDays(self, weights, days):
        def check(capacity):
            current_weight = 0
            days_needed = 1

            for x in weights:

                if current_weight + x > capacity:
                    days_needed += 1
                    current_weight = 0

                current_weight += x

            return days_needed <= days
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid = low + (high - low) // 2

            if check(mid):
                # Capacity kaam kar rahi hai
                # aur chhoti capacity try karo
                high = mid - 1

            else:
                # Capacity kam hai
                # capacity badhao
                low = mid + 1

        return low

        
print(Solution().shipWithinDays(weights,days))
