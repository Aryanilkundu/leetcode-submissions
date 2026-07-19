class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x!=0:
            if n<0:
                return self.myPow(1/x,-n)
            if n==0:
                return 1
            if n!=1:
                if n%2 == 0:
                    return self.myPow(x,int(n/2))**2
                else:
                    return x*self.myPow(x,int((n-1)/2))**2
            else:
                return x
        else:
            return 0
        