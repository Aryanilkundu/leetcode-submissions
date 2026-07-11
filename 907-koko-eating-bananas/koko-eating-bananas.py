class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = piles[0]
        m=piles[0]
        for i in range(1,len(piles)):
            s+=piles[i]
            m=max(m,piles[i])
        l=(s/h)
        r= m*(len(piles))
        k=r
        while l<=r:
            m=(l+r)//2
            f=int(math.ceil(piles[0]/m))
            for i in range(1,len(piles)):
                f+=int(math.ceil(piles[i]/m))
            if f>h:
                l=m+1
            elif f<=h:
                r=m-1
                k=min(k,m)
            # print(f,k,m)
        return int(k)
