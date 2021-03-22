# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 24/08/2018

from sys import stdin
from collections import deque

next_states = []

def to_num(l):
    return l[0]*1000 + l[1]*100 + l[2]*10 + l[3]

def get_digits(num):
    l = []
    for i in range(4):
        l.append((num // (10 ** i)) % 10)
    return list(reversed(l))

def gen_next_states():
    global next_states
    for i in range(0, 10001):
        index = []
        aux = get_digits(i)
        for j in range(4):
            upmove = aux[:]
            dwmove = aux[:]
            upmove[j] = aux[j] + 1 if aux[j] < 9 else 0
            dwmove[j] = aux[j] - 1 if aux[j] > 0 else 9
            index.append(to_num(upmove))
            index.append(to_num(dwmove))
        next_states.append(index)

def bfs(source, target):
    global visited, next_states
    if visited[source] == -1:
        return -1
    queue = deque() ; queue.append((source, 0)) ; visited[source] = 1
    while visited[target] == 0 and len(queue) != 0:
        u, d = queue.popleft()
        visited[u] = d
        for v in next_states[u]:
            if visited[v] == 0:
                queue.append((v, d + 1)) ; visited[v] = d + 1
        visited[u] = 1
    if visited[target] == 0:
        ans = -1
    else:
        ans = visited[target]
    return ans

def main():
    global visited
    tc = int(stdin.readline())
    gen_next_states()
    while tc > 0:
        visited = [0 for _ in range(10000)]
        stdin.readline()
        source = to_num([int(d) for d in stdin.readline().split()])
        target = to_num([int(d) for d in stdin.readline().split()])
        nf = int(stdin.readline())
        for x in range(nf):
            visited[to_num([int(d) for d in stdin.readline().split()])] = -1
        print(bfs(source, target))
        tc -= 1

main()
