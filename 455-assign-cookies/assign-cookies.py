class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j=0,0
        cnt = 0
        while i <= len(g)-1 and j<=len(s)-1:
            # print(i,j)
            if g[i]<=s[j]:
                i+=1
                j+=1
                cnt+=1
            else:
                j+=1
        # if j == len(s):
        #     break
        return cnt

