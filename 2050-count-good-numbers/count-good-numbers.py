class Solution:
    
    def countGoodNumbers(self, n: int) -> int:
        N = 1000000007
        if n%2 == 0:
            return pow(20,int(n/2),N) % N
        else:
            k = int((n-1)/2 )
            return 5*(pow(20,k,N)) % N
        # # if n==1:
        # #     return 5
        # # if (n-1)%2 == 0:
        # #     return self.countGoodNumbers(n-1)*5 % N
        # # else:
        # #     return self.countGoodNumbers(n-1)*4 % N
        # return pow(5,(n+1)//2,m:=10**9+7)*pow(4,n//2,m)%m