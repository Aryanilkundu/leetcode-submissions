class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # store binary as integer
          # -> 17

        # set bit i to 1
        def set_bit(x, i):
            return x | (1 << i)

        # set bit i to 0
        def clear_bit(x, i):
            return x & ~(1 << i)

        # toggle bit i
        def toggle_bit(x, i):
            return x ^ (1 << i)

        # read bit i
        def get_bit(x, i):
            return (x >> i) & 1
        m = len(matrix)
        n=len(matrix[0])
        r = int("0"*m, 2) 
        c = int("0"*n, 2)
        for i in range(m):
            for j in range(n):
                e = matrix[i][j]
                if e == 0:
                    r=set_bit(r,i)
                    c=set_bit(c,j)
                    # print(r,c)
        # print(r,c)
        for i in range(m):
            if get_bit(r,i) == 1:
                matrix[i] = [0]*n
        for j in range(n):
            if get_bit(c,j) == 1:
                for i in range(m):
                    matrix[i][j] = 0

