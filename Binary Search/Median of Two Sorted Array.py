nums1 = [1,3]
nums2 = [2]
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        # Binary search smaller array par
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1 = len(nums1)
        n2 = len(nums2)

        low = 0
        high = n1

        while low <= high:

            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1

            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            right1 = float('inf') if cut1 == n1 else nums1[cut1]

            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right2 = float('inf') if cut2 == n2 else nums2[cut2]

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                # Odd total length
                if (n1 + n2) % 2 == 1:
                    return max(left1, left2)

                # Even total length
                return (max(left1, left2) + min(right1, right2)) / 2.0

            # nums1 ka partition right side chala gaya
            elif left1 > right2:
                high = cut1 - 1

            # nums1 ka partition left side hai
            else:
                low = cut1 + 1
print(Solution().findMedianSortedArrays(nums1,nums2))