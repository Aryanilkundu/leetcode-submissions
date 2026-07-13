class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=weights[0]
        r=weights[0]
        n=len(weights)
        for i in range(1,n):
            l=max(l,weights[i])
            r+=weights[i]
        ans = r
        while l<=r:
            mid=(l+r)//2
            count=1
            current = 0
            for i in range(n):
                current+=weights[i]
                if current > mid:
                    count+=1
                    current=weights[i]
                if count>days:
                    break
            if count>days:
                l=mid+1
            else:
                r=mid-1
                ans = min(ans,mid)
        return ans 

