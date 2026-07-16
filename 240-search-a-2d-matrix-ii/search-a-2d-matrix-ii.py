class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin_search(row,l,r):
            while l<=r:
                mid = int((l+r)//2)
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    l=mid+1
                else:
                    r=mid-1
            return False
        m=len(matrix)
        n = len(matrix[0])
        ans_r = 0
        ans_c=0
        l=0
        r=m-1
        while l<=r:
            mid = int((l+r)//2)
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                ans_r = max(ans_r,mid)
                l=mid+1
        l=0
        r=n-1
        while l<=r:
            mid = int((l+r)//2)
            if matrix[0][mid] > target:
                r = mid - 1
            else:
                ans_c = max(ans_c,mid)
                l=mid+1
        l=0
        r = ans_r
        min_ans_r = 0
        while l<=r:
            mid = int((l+r)//2)
            if matrix[mid][-1] > target:
                r = mid -1
            else:
                min_ans_r = max(min_ans_r,mid)
                l=mid+1
        for i in range(min_ans_r,ans_r+1):
            row = matrix[i]
            if bin_search(row,0,ans_c):
                return True
        return False