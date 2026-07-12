def findMin(self, nums):
        low=0
        high=len(nums)-1
        if nums[0]<=nums[-1]:
            return nums[0]
        
        while low<=high:
            mid =low+(high-low)//2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]   # Pivot mil gaya

            elif nums[mid] >= nums[low]:
                low = mid + 1          # Left half sorted hai, pivot right me

            else:
                high = mid - 1