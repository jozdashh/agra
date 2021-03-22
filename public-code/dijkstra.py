from heapq import heappop,heappush

INF = float('inf')

def dijksra(G,s):
    ans = [INF for _ in G]; ans[s]=0
    prev = [None for _ in G]
    visited = [False for _ in G]
    heap = [(0,s)]
    while len(heap)!= 0:
        d,u = heappop(heap)
        if visited[u]==False:
            for v,dv in G[u]:
                if d+dv<ans[v]:
                    ans[v] = d+dv
                    heappush(heap, (ans[v],v))
                    pre[v] = u
            visited[u] = True
    return ans

def main():
    lenv, lene = map(int, stdin.readline().split())
    G = [ list() for _ in range(lenv) ]
    for _ in range(lene):
        u, v, d = map(int, stdin.readline().split())
        G[u].append((v, d))
        G[v].append((u, d))
    print(dijkstra(G, 0))


# test graph:
"""
6 9
0 1 7
0 2 9
0 5 14
1 2 10
1 3 15
2 3 11
2 4 2
3 4 6
4 5 9
"""
