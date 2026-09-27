class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0]) # matrix is nonempty

        l = 0 
        r = m * n - 1

        while l <= r:
            mid = (l + r) // 2
            y = mid // n # which row: divide by size of row
            x = mid % n # where in row: remainder
            if matrix[y][x] > target:
                r = mid - 1
            elif matrix[y][x] < target:
                l = mid + 1
            else:
                return True
        return False