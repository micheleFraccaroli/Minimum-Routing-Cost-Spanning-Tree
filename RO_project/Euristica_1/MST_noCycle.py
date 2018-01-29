'''
function for detect cycles into the graph
using the 'Union-find algorithm'
p: parent 
r: rank
v: edge
'''
import cost_calc
import reading_graph_txt as rgt
import toPlot

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

#kruskal algorithm

def kruskal(graph):
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

def copy_array(arr_edge,cost):
	res = []
	for e in arr_edge:
		res.append(e.copy())
	return (res,cost)

def print_all_solution(solutions):
	counter =0
	for arr,cost in solutions:
		counter+=1 
		print("soluzione n "+str(counter)+" costo = "+str(cost))
		print_array(arr)

def print_array(arr):
	for e in arr:
		print(e.toString())
def print_pointer(arr):
	for e in arr:
		print(str(e))

def pop_element(arr,e):
	for i in range(len(arr)-1):
		if(arr[i].same(e)):
			try:
				arr.pop(i)
			except:
				print("len = "+str(len(arr))+" i = "+str(i))

def heuristic(arr_edge,all_edge,nodes,solution_array):
	free_edge =[]
	for e_all in all_edge:
		find = False
		for edge in arr_edge:
			if(edge.same(e_all)):
				find = True
				break
		if(not find):
			e = e_all.copy()
			free_edge.append(e)

	for e in free_edge:
		arr_edge.append(e)
		a,b = cost_calc.cic(arr_edge)
		
		for h in b:
			if(h.same(e)):
				continue
			else:
				pop_element(arr_edge,h)
				newmin = cost_calc.blabla(nodes,arr_edge)
				solution_array.append(copy_array(arr_edge,newmin))
				arr_edge.append(h)

		pop_element(arr_edge,e)


def edge_list_compare(e,l):
	trovato = False
	for j in l:
		if j.same(e):
			trovato = True
			break
	return trovato

def list_list_compare(l1,l2):
	ok = True
	if(len(l1)!=len(l2)):
		return False
	for e in l1:
		if(not edge_list_compare(e,l2)):
			ok = False
			break
	return ok

def res_list_compare(res,l2):
	trovato = False
	if(res ==[]):
		return False
	for arr,cost in res:
		if(list_list_compare(arr,l2)):
			trovato = True
			break

	return(trovato)


def merge(res,sol):
	for arr,cost in sol:
		if not res_list_compare(res,arr):
			res.append((arr,cost))
		
		

def main():
	nodes,temp = rgt.read("../graph/graph_1.txt")
	all_edge = []
	for t in temp:
		c,a,b = t.split(" ")
		all_edge.append(cost_calc.Edge(a,b,c))
	all_edge.sort(key = lambda x: x.cost)
	arr_edge = []
	free_edge =[]
	for e in all_edge:
		arr_edge.append(e)
		a,b = cost_calc.cic(arr_edge)
		if(a):
			arr_edge.pop()
			free_edge.append(e.copy())
	mincost = cost_calc.blabla(nodes,arr_edge)

	solution_array = []
	solution_array.append(copy_array(arr_edge,mincost))
	heuristic(arr_edge,all_edge,nodes,solution_array)
	i =0
	welcome_to_matrix_neo = []
	res = []
	merge(res,solution_array)
	for arr,c in solution_array:
		if(i ==0):
			i+=1
			continue
		
		sol = []
		sol.append(copy_array(arr,c))
		heuristic(arr,all_edge,nodes,sol)
		merge(res,sol)
		welcome_to_matrix_neo.append(sol)

	welcome_to_matrix_neo.insert(0,solution_array)
	i=0
	#print_all_solution(solution_array)
	'''for arr,c in res:
		i+=1
		print("\niterazione n = "+str(i)+" costo = "+str(c)+"\n")
		print_array(arr)'''
	mincost = 9000
	minpos = -1
	i=0
	for a,c in res:
		if(mincost>c):
			mincost = c
			minpos = i
		i+=1
	print("best solution cost = "+str(mincost))
	a,b = res[minpos]
	print_array(a)
	plot_all_edge = []
	for e in all_edge:
		v1,v2 = (e.v1,e.v2)
		plot_all_edge.append((v1,v2))
	plot_solution = []
	for e in a:
		v1,v2 = (e.v1,e.v2)
		plot_solution.append((v1,v2))

	toPlot.toPlot(nodes,plot_all_edge,plot_solution)
	'''f.write(str(res))
	f.close()'''

if(__name__ == '__main__'):
	main()