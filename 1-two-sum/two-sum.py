class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls = []
        nums1 = nums.copy()
        for element in nums:
            element1 = target - element 
            if element1 != element:
                if element1 in nums:
                    ls.append(nums.index(element))
                    ls.append(nums.index(element1))
                    break
            else:
                nums1.pop(nums.index(element))
                if element1 in nums1:
                    ls.append(nums.index(element))
                    ls.append(nums.index(element1,nums.index(element)+1))
                    break

        return ls

        


        