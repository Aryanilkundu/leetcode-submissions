class Solution:
    def check(self, nums: List[int]) -> bool:
        violations =0
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                violations +=1
                if violations>1:
                    return False
        if violations == 1:
            if nums[-1] <= nums[0]:
                return True
            else:
                return False
        else:
            return True