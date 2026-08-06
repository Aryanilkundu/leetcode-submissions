class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # ct=defaultdict(int)
        # seen=set()
        # for i in range(len(nums)):
        #     if nums[i] not in seen:
        #         ct[nums[i]]+=1
        #         if ct[nums[i]] > len(nums)//3:
        #             seen.add(nums[i])
        #         if len(seen) ==2:
        #             break
        # return list(seen)
        count1 = count2 = 0
        cand1 = cand2 = None
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        # Verify counts
        return [n for n in (cand1, cand2) if nums.count(n) > len(nums) // 3]