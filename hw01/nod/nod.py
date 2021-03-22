# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 03/08/2018

from sys import stdin
from math import sqrt
from itertools import groupby

def MOD(n):
    factors = []
    i = 0
    while i < len(primes) and primes[i]*primes[i] <= n:
        if n % primes[i] == 0:
            n //= primes[i]
            factors.append(primes[i])
        else:
            i += 1

    # Por si al final n resulta ser primo
    if n > 1:
        factors.append(n)

    # Esta segunda parte toma ideas de:
    # https://stackoverflow.com/a/26760722
    # La lista por comprensión es sacada de:
    # https://stackoverflow.com/a/6352456
    times = [(k, sum(1 for i in g)) for k,g in groupby(factors)]
    ans = times[0][1] + 1
    for x in range(1, len(times)):
        ans *= times[x][1] + 1
    return ans


def solve(A, B):
    lo = 0
    hi = len(sec)

    while lo + 1 != hi:
        mid = (lo + ((hi - lo) >> 1))
        if A < sec[mid]:
            hi = mid
        else:
            lo = mid

    start = lo

    # En el caso que esto pase, se estará contando una ocurrencia menos
    # al hacer la resta de end y start. Al restarle a start, aumentamos
    # la resta final en +1
    if sec[lo] == A:
        start -= 1

    lo = 0
    hi = len(sec)

    while lo + 1 != hi:
        mid = (lo + ((hi - lo) >> 1))
        if B < sec[mid]:
            hi = mid
        else:
            lo = mid

    end = lo
    ans = end - start
    return ans

def main():
    # Criba de eratostenes
    N = 1007
    is_prime = [True for i in range(N + 5)]
    for i in range(2, N + 5):
        if is_prime[i]:
            for j in range(i*i, N + 5, i):
                is_prime[j] = False

    global primes
    primes = []
    for i in range(2, N + 5):
        if is_prime[i]:
            primes.append(i)

    # Generar todos los numeros NOD menores que 1'000.000
    global sec
    sec = [1, 2]
    while sec[-1] < (1000000 - 22):
        # el -22 evita que generemos un numero más grande que 1 millon
        sec.append(sec[-1] + MOD(sec[-1]))

    tcnt = int(stdin.readline())
    for tc in range(1, tcnt+1):
        A,B = map(int, stdin.readline().split())
        print('Case {0}: {1}'.format(tc, solve(A, B)))
main()
