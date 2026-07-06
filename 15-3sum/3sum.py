class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        d = defaultdict(list)
        for i in range(len(nums)):
            e = -nums[i]
            d[e].append(i)
        s =set()
        ls=[]
        for element in d:
            for j in range(len(nums)):
                complement = element - nums[j]
                if -complement in d:
                    found = False
                    for i in d[element]:
                        for k in d[-complement]:
                            if i!=j and j!=k and k!=i:
                                t = tuple(sorted((complement,-element,nums[j])))
                                if t not in s:
                                    s.add(t)
                                    ls.append([complement,-element,nums[j]])
                                found = True
                                break
                        if found == True:
                            break
        return ls