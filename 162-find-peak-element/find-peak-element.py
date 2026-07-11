class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1
        while l<=r:
            m = (l+r)//2
            if m > 0 and m < len(nums) - 1:
                if nums[m] > max(nums[m-1],nums[m+1]):
                    return m
                elif nums[m] < nums[m+1]:
                    l = m + 1
                else:
                    r = m -1
            else:
                if len(nums) == 1:
                    return m
                elif len(nums) == 2:
                    if nums[0]>nums[1]:
                        return 0
                    else:
                        return 1
                else:
                    if m == 0:
                        if nums[0] > nums[1]:
                            return 0
                        else:
                            return 1
                    else:
                        if nums[-1]>nums[-2]:
                            return len(nums)-1
                        else:
                            return len(nums) - 2
                    return m