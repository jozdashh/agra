# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 11/10/2018

from heapq import heappop, heappush
from sys import stdin
INF = float('inf')

def dijkstra(G, b_arr, heap):
    visited = [False for _ in range(len(G))]
    while len(heap) != 0:
        du, u = heappop(heap)
        if visited[u] == False:
            for v, dv in G[u]:
                if du + dv < b_arr[v]:
                    b_arr[v] = du + dv
                    heappush(heap, (b_arr[v], v))
            visited[u] = True
    return b_arr

def main():
    line = stdin.readline()
    while line != '':
        n_sites, n_roads, n_banks, n_pol_stns = map(int, line.split())
        G = [[] for _ in range(n_sites)]
        cnt = n_roads
        while cnt > 0:
            u, v, t = map(int, stdin.readline().split())
            G[u].append((v, t))
            G[v].append((u, t))
            cnt -= 1
        banks = list(map(int, stdin.readline().split()))
        pol_stns = list()
        if n_pol_stns != 0:
            pol_stns = list(map(int, stdin.readline().split()))
        heap = list()
        b_arr = [INF for _ in range(n_sites)]
        for p in pol_stns:
            b_arr[p] = 0
            heap.append((0, p))
        b_arr = dijkstra(G, b_arr, heap)
        aux, indxs = list(), list()
        for i in banks:
            aux.append(b_arr[i])
        mx = max(aux)
        cnt = 0
        for i in banks:
            if b_arr[i] == mx:
                indxs.append(i)
                cnt += 1
        print(cnt, mx if mx != INF else '*')
        indxs.sort()
        l = ''
        for i in indxs:
            l += str(i) + ' '
        print(l[:-1])
        line = stdin.readline()

main()
