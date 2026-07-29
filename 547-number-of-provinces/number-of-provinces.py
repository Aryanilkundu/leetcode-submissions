class Solution:
    # def dfs(self,v,visited):
    #     if not visited[v]:
    #         visited[v]=True
    #         for j in range(len(isConnected)):
    #             if isConnected[v][j] == 1 and not visited[j]:
    #                 self.dfs(j,visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(v,visited):
            if not visited[v]:
                visited[v]=True
                for j in range(len(isConnected)):
                    if isConnected[v][j] == 1 and not visited[j]:
                        dfs(j,visited)
        n = len(isConnected)
        cnt = 0
        visited = [False]*n
        for i in range(n):
            if not visited[i]:
                dfs(i,visited)
                cnt+=1
        return cnt

        