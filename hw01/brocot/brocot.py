# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 28/07/2018

from sys import stdin

class Fraction:
    def __init__(self, up, down):
        self.up = up
        self.down = down

    def __add__(self, other_frac):
        return Fraction(self.up + other_frac.up, self.down + other_frac.down)

    def __eq__(self, other_frac):
        return self.up == other_frac.up and self.down == other_frac.down

    def __lt__(self, other_frac):
        if self.down == other_frac.down:
            return self.up < other_frac.up
        # https://www.youtube.com/watch?v=RD-sTZEvqHk
        # De ahí saqué cómo hacer ésta comparación
        i = self.up * other_frac.down
        j = self.down * other_frac.up
        return i < j

# Usé el algortimo de busqueda presentado aquí:
# https://en.wikipedia.org/wiki/Stern%E2%80%93Brocot_tree#Mediants_and_binary_search
def solve(target):
  ans = ""
  n = Fraction(target[0], target[1])
  l = Fraction(0, 1)
  h = Fraction(1, 0)
  m = l + h
  while n != m:
      if m < n:
          ans += "R"
          l = m
      elif n < m:
          ans += "L"
          h = m
      m = l + h
  return ans

def main():
    target = [int(x) for x in stdin.readline().strip().split()]
    while target[0]!=1 or target[1]!=1:
        print(solve(target))
        target = [int(x) for x in stdin.readline().strip().split()]

main()
