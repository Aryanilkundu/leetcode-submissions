class Solution:
    from collections import deque
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    # print(i,j)
                    if grid[i][j] == 1:
                        q.append([i,j])
                        visited[i][j] = True

        while q:
            r,c = q.popleft()
            direc = [(0,1),(0,-1),(1,0),(-1,0)]
            for elem in direc:
                dx,dy = elem[0],elem[1]
                rr = r+dx
                cc = c+dy
                if 0<=rr<m and 0<=cc<n and grid[rr][cc]== 1 and not visited[rr][cc]:
                    visited[rr][cc] = True
                    q.append([rr,cc])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == False:
                    cnt+=1
        return cnt
        
