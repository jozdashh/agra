# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 30/09/2018

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 4)

def compute_indeg(M):
	indeg = {node : 0 for node in M}
	for u in M:
		for v in M[u]:
			indeg[v] += 1
	return indeg

def create_map(vars, arcs):
	v = vars.split()
	a = arcs.split()
	m = {var : [] for var in v}
	for arc in a:
		m[arc[2]].append(arc[0])
	return m

def toposort(M):
	ans = list()
	indeg = {node : 0 for node in M}
	for u in M:
		for v in M[u]:
			indeg[v] += 1
	pending = list()
	for u in M:
		if indeg[u] == 0:
			pending.append(u)
	while len(pending) != 0:
		u = pending.pop()
		ans.append(u)
		for v in M[u]:
			indeg[v] -= 1
			if indeg[v] == 0:
				pending.append(v)
	return ans

def dfs(M, r, indeg):
	global PARENT, PATH
	indeg[r] = -1
	for v in M[r]:
		indeg[v] -= 1
	flag = True
	for k in indeg:
		if indeg[k] == 0: flag = False
	if flag:
		aux1, aux2 = '', r
		for i in range(len(PARENT)):
			aux1 += aux2 + ' '
			aux2 = PARENT[aux2]
		PATH.append(aux1[:-1])
	for v in M:
		if indeg[v] == 0:
			PARENT[v] = r
			dfs(M, v, indeg.copy())

def solve(M):
	global PARENT, PATH
	if len(toposort(M)) != len(M): return ['NO']
	indeg = compute_indeg(M)
	roots = list()
	PATH = list()
	for u in M:
		if indeg[u] == 0:
			roots.append(u)
	for r in roots:
		PARENT = {k : '' for k in M}
		dfs(M, r, indeg)
		indeg = compute_indeg(M)
	PATH.sort()
	return PATH

def main():
	tc = int(stdin.readline())
	while tc > 0:
		stdin.readline()
		vars = stdin.readline()
		arcs = stdin.readline()
		M = create_map(vars, arcs)
		ans = solve(M)
		if ans[0] != 'NO':
			for i in ans:
				print(i)
		else:
			print(ans[0])
		tc -= 1
		if tc != 0: print('')

main()
