class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l =0
        n=len(nums)
        r = len(nums)-1
        while l<=r:
            m=(l+r)//2
            if 1<=m<=n-2:
                if nums[m-1]!=nums[m] and nums[m+1]!=nums[m]:
                    return nums[m]
                elif nums[m-1]==nums[m]:
                    if m%2==0:
                        r=m-2
                    else:
                        l=m+1
                elif nums[m+1]==nums[m]:
                    if m%2==0:
                        l=m+2
                    else:
                        r=m-1
            elif m==0:
                if n>=2:
                    if nums[0]!=nums[1]:
                        return nums[0]
                    else:
                        print('hey')
                else:
                    return nums[0]
            else:
                return nums[-1]
        return nums[m]
            