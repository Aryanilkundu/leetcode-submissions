class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last=0
        cnt=0
        ans=0
        for i in range(len(arr)):
            if arr[i] == last+1:
                last+=1
            elif arr[i] > last+1:
                cnt+=arr[i]-last-1
                last=arr[i]
                if cnt>=k:
                    ans = arr[i]-(cnt-k)-1
                    break
        if ans==0:
            return arr[-1]+k-cnt
        else:
            return ans

