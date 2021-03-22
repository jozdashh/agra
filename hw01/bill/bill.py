# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 04/08/2018

from sys import stdin

def cost_to_cons(cost):
    ans = 0
    if cost < 200:
        ans = cost // 2
    elif cost > 200 and cost <= 3*9900:
        ans = 100 + (cost - 2*100) // 3
    elif cost > 3*9900 and cost <= 5*990000:
        ans = 100 + 9900 + (cost - (2*100 + 3*9900)) // 5
    elif cost > 5*990000:
        ans = 100 + 9900 + 990000 + (cost - (2*100 + 3*9900 + 5*990000)) // 7
    return ans

def cons_to_cost(consume):
    ans = 0
    if consume < 100:
        ans = consume * 100
    elif consume > 100 and consume <= 10000:
        ans = 2*100 + (consume - 100) * 3
    elif consume > 10000 and consume <= 1000000:
        ans = 2*100 + 3*9900 + (consume - (100 + 9900)) * 5
    elif consume > 1000000:
        ans = 2*100 + 3*9900 + 5*990000 + (consume - (100 + 9900 + 990000)) * 7
    return ans

def solve(tsum, diff):
    lo = 0
    hi = cost_to_cons(tsum)
    while lo + 1 != hi:
        c2 = (lo + ((hi - lo) >> 1))
        c1 = (cost_to_cons(tsum) - c2)
        if abs(cons_to_cost(c1) - cons_to_cost(c2)) > diff:
            hi = c2
        elif abs(cons_to_cost(c1) - cons_to_cost(c2)) < diff:
            lo = c2
        else:
            break
    return cons_to_cost(c1)


def main():
  tsum,diff = map(int,stdin.readline().split())
  while tsum+diff!=0:
    print(solve(tsum, diff))
    tsum,diff = map(int,stdin.readline().split())
main()
