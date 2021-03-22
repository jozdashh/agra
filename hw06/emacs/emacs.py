# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 04/11/2018

from sys import stdin

def kmp_prefix(s):
	n = len(s) ; P = [None]*n
	i = 0 ; j = P[0] = -1
	while i < n-1:
		while j> -1 and s[i] != s[j]: j = P[j]
		i += 1 ; j += 1
		if s[i] == s[j]: P[i] = P[j]
		else: P[i] = j
	return P

def kmp_search(x, y, j):
	i = 0
	P = kmp_prefix(x)
	while j < len(y):
		while i > -1 and x[i] != y[j]: i = P[i]
		i += 1 ; j += 1
		if i >= len(x):
			i = P[i-1]
			return (True, j)
	return (False, -1)

def solve(t, p):
	ans = True
	q = p.strip('*').split('*')
	if len(q)==0 and len(p)!=len(t): ans = False
	i, j = 0, 0
	while i < len(q) and ans:
		if len(q[i])!=0:
			aux = kmp_search(q[i], t, j)
			ans = ans and aux[0]
			j = max(aux[1], j)
		i += 1
	return ans

def main():
	line = stdin.readline()
	while len(line)!=0:
		n = int(line)
		t = stdin.readline()
		for i in range(n):
			w = stdin.readline().strip()
			ans = solve(t, w)
			if ans: print('yes')
			else: print('no')
		line = stdin.readline()

main()
