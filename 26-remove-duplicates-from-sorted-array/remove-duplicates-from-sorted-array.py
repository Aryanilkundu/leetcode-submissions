class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set()
        for i in range(len(nums)):
            if nums[i] in s:
                nums[i] = 101
            else:
                s.add(nums[i])
        nums.sort()
        return len(s)