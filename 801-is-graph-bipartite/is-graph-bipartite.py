class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        ans = True
        def dfs(v,prev_colour):
            visited[v] = True
            colour[v] = 3 - prev_colour
            for u in graph[v]:
                if not visited[u]:
                    if dfs(u,colour[v]):
                        continue
                    else:
                        return False
                else:
                    if colour[u] == colour[v]:
                        return False
            return True
        n = len(graph)
        visited = [False]*n
        colour = [0]*n
        for i in range(n):
            # colour[i] = 1
            if not visited[i]:
                colour[i] = 1
                if dfs(i,1):
                    continue
                else:
                    return False
        return True