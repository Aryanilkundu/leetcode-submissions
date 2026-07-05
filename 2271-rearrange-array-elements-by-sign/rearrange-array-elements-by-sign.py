class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = []
        neg=[]
        for i in range(n):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        k=0
        ls=[]
        while k!=n/2:
            ls.append(pos[0])
            ls.append(neg[0])
            pos.pop(0)
            neg.pop(0)
            k+=1
        return ls

