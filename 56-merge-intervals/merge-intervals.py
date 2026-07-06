class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        k=0
        while k+1<=len(intervals)-1:
            if intervals[k][-1] >= intervals[k+1][0]:
                intervals[k][-1] = max(intervals[k+1][-1],intervals[k][-1])
                intervals.pop(k+1)
            else:
                k+=1
        return intervals

        