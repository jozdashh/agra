# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 20/08/2018

from sys import stdin

def dfs(source):
    global adyl, visited, reach
    d = 1
    u = source
    visited[u] = 1
    while visited[adyl[u]] == 0 and reach[adyl[u]] == 0:
        u = adyl[u] ; visited[u] = 1 ; d += 1
    v = adyl[u]
    if v == source:
        for x in range(d):
            visited[v] = 0
            reach[v] = d
            v = adyl[v]
    elif v != source:
        aux = source
        for x in range(d):
            visited[aux] = 0
            aux = adyl[aux]
        aux = source
        d += reach[v]
        while aux != v:
            reach[aux] = d
            d -= 1
            aux = adyl[aux]

def solve():
    global adyl, visited, reach
    for i in range(len(adyl)):
        if reach[i] == 0:
            dfs(i)
    ans = []
    aux = max(reach)
    ind = reach.index(aux)
    ans.append(ind + 1)
    max_reach = aux
    reach[ind] = -1
    aux = max(reach)
    while max_reach == aux:
        ind = reach.index(aux)
        ans.append(ind + 1)
        reach[ind] = -1
        aux = max(reach)
    return min(ans)

def main():
    global adyl, visited, reach
    tc = int(stdin.readline())
    cc = 1
    while tc > 0:
        N = int(stdin.readline())
        adyl = [-1 for _ in range(N)]
        visited = [0 for _ in range(N)]
        reach = [0 for _ in range(N)]
        while N > 0:
            sn, tn = tuple(map(int, stdin.readline().split()))
            adyl[sn - 1] = (tn - 1)
            N -= 1
        print("Case {0}: {1}".format(cc, solve()))
        cc += 1
        tc -= 1

main()
