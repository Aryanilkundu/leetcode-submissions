class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in range(len(nums)):
            e = nums[i]
            if d[e] == 1:
                d.pop(e)
            else:
                d[e]+=1
        print(d)
        for key in d.keys():
            if d[key] == 1:
                return key


            
