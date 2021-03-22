# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 24/08/2018

from sys import stdin
from collections import OrderedDict

def solve(q):
    global arrN, N
    l, g = 0, 0
    lo, hi = 0, N
    mid = lo + ((hi - lo) // 2)
    while lo + 1 != hi:
        if q < arrN[mid]:
            hi = mid
        elif q > arrN[mid]:
            lo = mid
        elif q == arrN[mid]:
            return (mid - 1, mid + 1)
        mid = lo + ((hi - lo) // 2)
    l = lo
    if q < arrN[-1]:
        i = lo
        while arrN[i] <= q:
            i += 1
        g = i
    else:
        g = N + 1
    return (l, g)

def main():
    global arrN, N
    stdin.readline()
    arrN = list(OrderedDict.fromkeys(list(map(int, stdin.readline().split()))))
    N = len(arrN)
    Q = int(stdin.readline())
    arrQ = list(map(int, stdin.readline().split()))
    for query in arrQ:
        l, g = solve(query)
        l = arrN[l]
        g = 'X' if g >= N else arrN[g]
        print("{0} {1}".format(l, g))
main()
