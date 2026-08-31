class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums
        ans = m[0]
        for i in range(1,len(nums)):
            m[i] = max(m[i-1]+nums[i],nums[i])
            ans = max(ans,m[i])
        return ans


        