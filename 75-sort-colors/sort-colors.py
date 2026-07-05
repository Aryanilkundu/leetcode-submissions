class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] == 2:
                if i<=n-2:
                    if 0 in nums[i+1:]:
                        zero_idx = nums[i+1:].index(0)
                        nums[i] = 0
                        nums[zero_idx+i+1] = 2
                    else:
                        if 1 in nums[i+1:]:
                            one_idx = nums[i+1:].index(1)
                            nums[i] = 1
                            nums[one_idx+i+1] = 2
            elif nums[i] == 1:
                if i<=n-2:
                    if 0 in nums[i+1:]:
                        zero_idx = nums[i+1:].index(0)
                        nums[i] = 0
                        nums[zero_idx+i+1] = 1
        # print(nums[n-1:])