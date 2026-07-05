class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n>=3:
            k=n-3
            while k>=-1:
                if nums[k+1]>=nums[k+2]:
                    k=k-1
                    continue
                else:
                    i = nums[k+1]
                    next_max = 101
                    next_max_idx = 0
                    for j in range(k+2,n):
                        if nums[j] > i:
                            if nums[j]<next_max:
                                next_max =nums[j]
                                next_max_idx = j

                    nums[k+1] = next_max
                    nums[next_max_idx] = i
                    nums[k+2:] = sorted(nums[k+2:])
                    break
            if k== -2:
                nums.sort()
        elif n==2:
            a,b=nums[0],nums[1]
            nums[0],nums[1] = b,a
        



