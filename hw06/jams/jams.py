# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 26/10/2018

from sys import stdin

INF = float('inf')

def floyd_warshall(G):
    global n
    dist = [[INF for _ in range(n)] for _ in range(n)]
    for u, v in G: dist[u][v] = 1 ; dist[u][u] = dist[v][v] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def solve():
    global G, R, n, A, B
    distG, distR = floyd_warshall(G), floyd_warshall(R)
    flag, ans, i = True, None, 0
    while i < n and flag:
        j = 0
        while j < n and flag:
            flag = i == j or A*distG[i][j] + B >= distR[i][j] ; j += 1
        i += 1
    ans = 'Yes' if flag else 'No'
    return ans

def main():
    global G, R, n, A, B
    line = stdin.readline()
    while line!='0\n':
        n, G, R = int(line), list(), list()
        for i in range(n):
            inter = stdin.readline().split()
            for j in inter[1:]: G.append((int(inter[0])-1, int(j)-1))
        for i in range(n):
            inter = stdin.readline().split()
            for j in inter[1:]: R.append((int(inter[0])-1, int(j)-1))
        A, B = map(int, stdin.readline().split())
        print(solve())
        line = stdin.readline()

main()
