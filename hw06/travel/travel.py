# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 25/10/2018

from sys import stdin

# Todavía no sé qué algortimo usar. Pero creo que es dijkstra
# con algunas pequeñas modificaciones.
# Ja hpta pequeñas. Esta mierda al igual que dna es pura programación dinámica.

def solve(p, n):
    pass

def main():
    global f, G, si
    line = stdin.readline()
    while line != '':
        p, f, q = map(int, stdin.readline().split())
        G = [[] for _ in range(f)]
        planet = dict()
        for i in range(p): planet[stdin.readline()] = i
        for i in range(f):
            s0, sd, c, t = map(int, stdin.readline().split())
            G[planet[s0]].append((planet[sd], c, t))
        si = planet[stdin.readline()]
        for i in range(q):
            query = stdin.readline().split()
            _planet, n = query[0], int(query[1])
            print(solve(planet[_planet], n))
        line = stdin.readline()

main()
