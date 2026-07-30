class Solution:
    from collections import deque
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def edge(s1, s2):
            diff_count = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff_count += 1
                    if diff_count > 1:
                        return False
            return diff_count == 1
        # print(edge("a","c"))
        if beginWord not in wordList:
            wordList.append(beginWord)
        n = len(wordList)
        adj = [[] for _ in range(n)]
        for i in range(n-1):
            for j in range(i+1,n):
                if edge(wordList[i],wordList[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        print(adj)
        if endWord not in wordList:
            print('k')
            return 0
        start = wordList.index(beginWord)
        q = deque()
        q.append(start)
        dist = [0]*n
        par = [-1]*n
        dist[start] = 1
        while q:
            k = q.popleft()        
            for u in adj[k]:
                if dist[u] == 0:
                    par[u] = k
                    q.append(u)
                    dist[u] = dist[k]+1
                    if wordList[u] == endWord:
                        return dist[u]

        return dist[wordList.index(endWord)]

        
                



        