class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        n = len(nums)
        for i in range(n):
            total+=nums[i]
        if total%2 != 0:
            return False
        target = int(total/2)
        possible =[[False for _ in range(n)] for _ in range(target+1)]
        if nums[0]<= target:
            possible[nums[0]][0] = True
        for i in range(n):
            possible[0][i] = True
        for i in range(1,n):
            for j in range(target+1):
                if j - nums[i]>=0:
                    possible[j][i] = possible[j-nums[i]][i-1] or possible[j][i]
                possible[j][i] = possible[j][i-1] or possible[j][i]
        # print(possible)
        return possible[target][-1]
