class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        curr = 1
        while i<len(chars)-1:
            if chars[i] == chars[i+1] :
                curr+=1
                if i==len(chars)-2 and curr>1:
                    for j in range(i-curr+2,i+2):
                        chars[j] = chars[j]+f"{curr}"
            else:
                if curr > 1:
                    for j in range(i-curr+1,i+1):
                        chars[j] = chars[j]+f"{curr}"
                    curr = 1
            i+=1
        print(chars)
        i=0
        while i < len(chars)-1:
            if chars[i] == chars[i+1]:
                chars.remove(chars[i])
                if i == len(chars)-1:
                    element = chars[i]
                    if len(element) != 1:
                        chars[i] = element[0]
                        i+=1
                        for e in element[1:]:
                            chars.insert(i,e)
                            i+=1

            else:
                element = chars[i]
                if len(element) != 1:
                    chars[i] = element[0]
                    i+=1
                    for e in element[1:]:
                        chars.insert(i,e)
                        i+=1
                else:
                    i+=1
        return len(chars)
        

            


