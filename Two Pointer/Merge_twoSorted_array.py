nums1 = [4,5,6,0,0,0]
m = 3

nums2 = [1,2,3]
n = 3


def merge(nums1, m, nums2, n):
    result = []

    i = 0
    j = 0

    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    while i < m:
        result.append(nums1[i])
        i += 1

    while j < n:
        result.append(nums2[j])
        j += 1

    # result ko nums1 me copy karo
    for i in range(m + n):
        nums1[i] = result[i]


merge(nums1, m, nums2, n)
print(nums1)