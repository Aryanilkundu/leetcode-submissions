class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        # heights.append(-1)
        # heights.insert(0,-1)
        area = [i+1 for i in range(len(heights))]
        for idx, element in reversed(list(enumerate(heights))):
            if element!=0:
                # print(element,stack)
                while stack and element <= stack[-1][1]:
                    stack.pop()
                if len(stack)!=0:
                    area[idx] = stack[-1][0]
                elif len(stack) == 0 and idx != len(heights)-1:
                    area[idx] = len(heights)
                area[idx] = element*(area[idx] - idx)
            else:
                area[idx] = 0
            stack.append((idx,element))
        # print(area)
        stack =[]
        for idx,element in enumerate(heights):
            if element !=0:
                # print(element,stack)
                while stack and element <= stack[-1][1]:
                    stack.pop()
                if len(stack) !=0 and idx - stack[-1][0]!=1:
                    area[idx] += element*(idx - stack[-1][0]-1)
                elif len(stack)==0 and idx != 0:
                    area[idx] += element*(idx)
            stack.append((idx,element))
        # print(area)
        return max(area)            
