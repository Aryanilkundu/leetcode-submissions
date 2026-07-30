class Solution:
    from collections import deque
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if i in [0,m-1] or j in [0,n-1]:
                    if board[i][j] == 'O':
                        visited[i][j] = True
                        q.append([i,j])
        print(q)
        while q:
            r,c = q.popleft()
            direc = [(0,1),(0,-1),(1,0),(-1,0)]
            for e in direc:
                dx,dy = e[0],e[1]
                nx = r+dx
                ny = c+dy
                if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and board[nx][ny]=="O":
                    visited[nx][ny] = True
                    q.append([nx,ny])

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and  not visited[i][j]:
                    board[i][j] = 'X'
        
        
        
                
                    
