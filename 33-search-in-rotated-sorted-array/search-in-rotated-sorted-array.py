class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sorted_list = sorted(nums,reverse =False)
        k = sorted_list.index(nums[-1])+1
        if target not in nums:
            return -1
        elif target <= nums[-1]:
            # print(k,sorted_list)
            return (len(nums)-k)+sorted_list.index(target)
        elif len(nums)==1 and target in nums:
            return 0
        else:
            return sorted_list.index(target) - k