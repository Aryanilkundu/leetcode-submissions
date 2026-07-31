class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = []
        for i in range(n):
            dp.append([0]*(i+1))
        dp[0][0] = triangle[0][0]
        cuml = triangle[0][0]
        cumr = triangle[0][0]
        for i in range(1,n):
            dp[i][0] = cuml+triangle[i][0]
            dp[i][-1] = cumr + triangle[i][-1]
            cuml, cumr = dp[i][0],dp[i][-1]
        if n==2:
            return min(dp[1][0],dp[1][-1])
        elif n == 1:
            return triangle[0][0]
        else:

            for i in range(2,n):
                for j in range(1,i):
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
            # print(dp)
            return min(dp[-1])


        