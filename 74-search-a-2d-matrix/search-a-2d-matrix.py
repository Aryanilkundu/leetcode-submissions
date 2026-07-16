class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def bin_search(row):
            l =0
            r = n-1
            while l<=r:
                mid = int((l+r)//2)
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    l=mid+1
                else:
                    r=mid-1
            return False
        l = 0
        r = m-1
        while l<=r:
            mid = int((l+r)//2)
            row = matrix[mid]
            if row[0]<=target<=row[-1]:
                return bin_search(row)
            elif target < row[0]:
                r = mid - 1
            else:
                l = mid+1
        return False