class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxe=nums[0]
        mine= nums[0]
        for i in range(1, len(nums)):
            if nums[i]<0:
                maxe1 = max(mine*nums[i],nums[i])
                mine1 = min(maxe*nums[i],nums[i])
                maxe,mine = maxe1,mine1
            elif nums[i]>0:
                maxe1 = max(maxe*nums[i],nums[i])
                mine1 = min(mine*nums[i],nums[i])
                maxe,mine = maxe1,mine1
            else:
                maxe = 0
                mine = 0
            print(maxe,mine)
            res = max(res,maxe)
            print(res)
        return res