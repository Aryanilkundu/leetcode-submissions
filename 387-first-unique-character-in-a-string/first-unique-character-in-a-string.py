class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(list)
        for i in range(len(s)):
            d[s[i]].append(i)
        ans = 10e5+1
        for e in d.keys():
            if len(d[e]) == 1:
                ans = min(ans,d[e][0])
        if ans == 10e5+1:
            ans = -1
        return ans

                
            