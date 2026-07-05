class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ct =0
        while ct!=k:
            nums.insert(0,nums[-1])
            nums.pop()
            ct+=1