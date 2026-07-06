class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ct=defaultdict(int)
        seen=set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                ct[nums[i]]+=1
                if ct[nums[i]] > len(nums)//3:
                    seen.add(nums[i])
        return list(seen)