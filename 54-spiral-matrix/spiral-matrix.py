class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        top_r =0
        bottom_r=m-1
        left_c=0
        right_c=n-1
        ls = []
        while top_r<bottom_r and left_c < right_c:
            for j in range(left_c,right_c+1):
                ls.append(matrix[top_r][j])
            top_r+=1
            for i in range(top_r,bottom_r+1):
                ls.append(matrix[i][right_c])
            right_c-=1
            for j in range(right_c,left_c-1,-1):
                ls.append(matrix[bottom_r][j])
            bottom_r-=1
            for i in range(bottom_r,top_r-1,-1):
                ls.append(matrix[i][left_c])
            left_c+=1
        if top_r == bottom_r and len(ls)!=m*n:
            for j in range(left_c,right_c+1):
                ls.append(matrix[top_r][j])
        if left_c == right_c and len(ls)!=m*n:
            for i in range(top_r,bottom_r+1):
                ls.append(matrix[i][left_c])
        return ls