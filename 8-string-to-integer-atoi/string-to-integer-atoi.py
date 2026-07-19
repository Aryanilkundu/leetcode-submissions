class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ""
        digits = ["0","1","2","3","4","5","6","7",'8',"9"]
        # to_sign_check = False
        s_clean = s.lstrip()
        i=0
        if s_clean == "":
            return 0
        if s_clean[0] == '-' or s_clean[0] == '+':
            ans += s_clean[0]
            i=1
        while i <= len(s_clean) -1:
            if s_clean[i] in digits:
                ans+=s_clean[i]
                i+=1
            else:
                break
        # print(ans)
        if ans in ["","-","+"]:
            ans = 0
        ans = max(-2**31,int(ans))
        ans = min(2**31-1,int(ans))
        return int(ans)
        
        
        