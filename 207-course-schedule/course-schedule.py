class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        n = numCourses
        for i in range(len(prerequisites)):
            e = prerequisites[i]
            adj[e[0]-1].append(e[1]-1)
        visited = [False]*n
        rec = [False]*n
        def dfs(v):
            if rec[v]:
                return False
            if visited[v]:
                return True
            visited[v] = True
            rec[v] = True
            for u in adj[v]:
                    if not dfs(u):
                        return False
            rec[v] = False
            return True
        for i in range(n):
            if not visited[i] and not dfs(i):
                return False
        return True

