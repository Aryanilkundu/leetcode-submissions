class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        max_run =0
        current_run=0
        for i in range(n):
            if nums[i] == 1:
                current_run+=1
            else:
                max_run = max(max_run, current_run)
                current_run = 0
        return max(max_run, current_run)