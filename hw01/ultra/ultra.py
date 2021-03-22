# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 30/07/2018

from sys import stdin

MAX   = 50010
num   = [ None for i in range(MAX) ]

# Este mismo algoritmo para este problema en particular fue
# presentado por el profesor Carlos Pinzon en la clase del 25 de Julio.
def solve(lo, hi):
  if hi - lo <= 1:
    return 0

  mid = (lo + hi) // 2
  ans = solve(lo, mid)
  ans += solve(mid, hi)

  aux = []
  i = lo
  j = mid
  while i < mid and j < hi:
    if num[i] <= num[j]:
      aux.append(num[i])
      i += 1
    else:
      aux.append(num[j])
      # Todos los numeros de desde num[i] hasta num[mid]
      # son mayores que el num[j] encontrado, por lo cual hay mid - i inversiones.
      ans += mid - i
      j += 1

  while i < mid:
    aux.append(num[i])
    i += 1

  while j < hi:
    aux.append(num[j])
    j += 1

  num[lo:hi] = aux
  return ans

def main():
  global num
  inp = stdin
  n = int(stdin.readline().strip())
  while n>0:
    for i in range(n):
      num[i] = int(stdin.readline())
    print(solve(0, n))
    n = int(stdin.readline().strip())

main()
