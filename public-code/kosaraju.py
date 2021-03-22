from collections import deque

def kosaraju(G):
    """
    Calculates all the scc's of the given graph G in
    adyacency list representation.
    """
    n = len(G)
    d = deque()
    vis = [0 for _ in range(n)]
    scc = [-1 for _ in range(n)]
    scc_cnt = 0
    R = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            R[v].append(u)

    def dfs1(s):
        vis[s] = 1
        for v in G[s]:
            if vis[v] == 0:
                dfs1(v)
        d.appendleft(s)

    def dfs2(s):
        vis[s] = 1
        scc[s] = scc_cnt
        for v in R[s]:
            if vis[v] == 0:
                dfs2(v)

    for v in range(n):
        if vis[v] == 0:
            dfs1(v)

    vis = [0 for _ in range(n)]
    for v in d:
        if vis[v] == 0:
            dfs2(v)
            scc_cnt += 1
    # for i in range(n):
    #     print(i, scc[i])
    print(scc)
    # Done.

G = [ [3],[0,2],[0,4,9],[5],[1],[3,7],[5],[8],[7],[]]
kosaraju(G)
