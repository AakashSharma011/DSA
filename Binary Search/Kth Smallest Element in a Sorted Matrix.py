matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
class Solution(object):
    def kthSmallest(self, matrix, k):

        n = len(matrix)
        m = len(matrix[0])

        low = matrix[0][0]
        high = matrix[n - 1][m - 1]

        while low <= high:

            guess = (low + high) // 2

            row = n - 1
            col = 0
            count = 0

            # count elements <= guess
            while row >= 0 and col < m:

                if matrix[row][col] <= guess:
                    count += row + 1
                    col += 1

                else:
                    row -= 1

            if count < k:
                low = guess + 1

            else:
                high = guess - 1

        return low
print(Solution().kthSmallest(matrix,k))