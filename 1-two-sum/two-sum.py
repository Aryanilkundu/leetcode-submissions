class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ls = []
        # nums1 = nums.copy()
        # for element in nums:
        #     element1 = target - element 
        #     if element1 != element:
        #         if element1 in nums:
        #             ls.append(nums.index(element))
        #             ls.append(nums.index(element1))
        #             break
        #     else:
        #         nums1.pop(nums.index(element))
        #         if element1 in nums1:
        #             ls.append(nums.index(element))
        #             ls.append(nums.index(element1,nums.index(element)+1))
        #             break

        # return ls

        l = 0 
        r = len(nums)-1
        ls = []
        for index, val in enumerate(nums):
            ls.append([index,val])
        ls = sorted(ls,key=lambda i: (i[1], i[0]))

        while l<r:
            if ls[l][1]+ls[r][1] == target:
                return [ls[l][0],ls[r][0]]
            elif ls[l][1]+ls[r][1] > target:
                r -=1
            else:
                l+=1
        return [l,r]
            

        


        