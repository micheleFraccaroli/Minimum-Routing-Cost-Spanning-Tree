'''
function for detect cycles into the graph
using the 'Union-find algorithm' and MST with 'kruskal algorithm'
'''

### Union-find algorithm ###
p = dict()
r = dict()

def Make_set(v):
	p[v] = v
	r[v] = 0

def Find(v):
	if(p[v] != v):
		p[v] = Find(p[v])
	return p[v]

def Union(v1, v2):
	v1_Root = Find(v1)
	v2_Root = Find(v2)

	if(r[v1_Root] < r[v2_Root]):
		p[v1_Root] = v1_Root
	elif(r[v1_Root] > r[v2_Root]):
		p[v2_Root] = v1_Root
	else:
		p[v2_Root] = v1_Root
		r[v1_Root] = r[v1_Root] + 1

### Kruskal algorithm ###

def kruskal():
	a, b = read("graph.txt")
	for v in graph['vertices']:
		Make_set(v)
		MST = set()
		edges = list(graph['edges'])
		edges.sort()

	for edge in edges:
		w, v1, v2 = edge
		if Find(v1) != Find(v2):
			Union(v1, v2)
			MST.add(edge)

	return sorted(MST)

def main():
	'''graph = {
		'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
		'edges': {(2, 'A', 'B'), (3, 'A', 'C'), (4, 'B', 'C'), (8, 'B', 'D'), (4, 'C', 'E'), (7, 'C', 'D'), (8, 'E', 'D'), (3, 'D', 'F'), (6, 'E', 'F')}
	}'''
	f = open("MST.txt", "w")
	f.write(str(kruskal())
	f.close()

if(__name__== '__main__'):
	main()
	print(p)
	print(r)