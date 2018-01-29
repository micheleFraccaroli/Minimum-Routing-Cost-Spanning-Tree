import os
import SPT_dijk as spt
import reading_graph_txt as rgt
import cost_calc
import toPlot
import parent_reproduction as pare
import timeit

def in_list(el,arr):
	found = False
	for a in arr:
		if(a == el):
			found = True
			break
	return found

def edge_in_list(edge,arr_edge):
	found = False
	for a in arr_edge:
		if(a.same(edge)):
			found = True
			break
	return found


def connected_to(node,arr_edge,visited):
	if(not in_list(node,visited)):
		visited.append(node)
	for e in arr_edge:
		if(e.connected_left(node)):
			if(not in_list(e.v2,visited)):
				connected_to(e.v2,arr_edge,visited)
		if(e.connected_right(node)):
			if(not in_list(e.v1,visited)):
				connected_to(e.v1,arr_edge,visited)

def print_array(arr):
	for e in arr:
		print(e.toString())

def get_free_edges(arr_edge,all_edge):
	res = []
	for a in all_edge:
		found = False
		for j in arr_edge:
			if(a.same(j)):
				found = True
				break

		if(not found):
			res.append(a.copy())

	return res


def copy_array(arr_edge,cost):
	res = []
	for e in arr_edge:
		res.append(e.copy())
	return (res,cost)

def cut_edges(nodes1,nodes2,free_edges):
	res = []
	for e in free_edges:
		for n1 in nodes1:
			for n2 in nodes2:
				if((e.connected_left(n1) and e.connected_right(n2)) or (e.connected_left(n2) and e.connected_right(n1))):
					res.append(e.copy())
	return res

def heu_cut(arr_edge,all_edge,nodes):
	solution_array = []
	free_edges = get_free_edges(arr_edge,all_edge)
	arr_edge_cost = cost_calc.blabla(nodes,arr_edge)
	solution_array.append((arr_edge,arr_edge_cost))
	for e in arr_edge:
		temp = []
		for k in arr_edge:
			if(k.same(e)):
				pass
			else:
				temp.append(k.copy())
		nodes1 = []
		nodes2 = []
		connected_to(e.v1,temp,nodes1)
		connected_to(e.v2,temp,nodes2)
		c_edges = cut_edges(nodes1,nodes2,free_edges)
		#print("temp")
		#print_array(temp)
		#print("cutedges")
		#print_array(c_edges)
		for c_edge in c_edges:
			temp.append(c_edge)
			cost = cost_calc.blabla(nodes,temp)

			solution_array.append(copy_array(temp,cost))
			temp.remove(c_edge)
	
	t_arr,mincost = solution_array[0]
	print("mincost = "+str(mincost))
	minpos = 0
	i=0
	for a,b in solution_array[1:]:
		i+=1
		if(b<mincost):
			minpos = i
			mincost = b


	return solution_array[minpos]



	#for e in arr_edge:



def main():
	nodes,temp = rgt.read("../../graph/graph_random_3.txt")
	all_edge = []
	plot_all_edge = []
	plot_solution = []
	for t in temp:
		c,a,b = t.split(" ")
		e = cost_calc.Edge(a,b,c)
		all_edge.append(e)
	list_of_list_of_list =spt.loop_root_SPT(nodes,temp)
	trees = []
	for list_of_list in list_of_list_of_list:
		temp_tree = []
		for lis in list_of_list:
			for ed in lis:
				if(edge_in_list(ed,temp_tree)):
					pass
				else:
					temp_tree.append(ed)
		trees.append(temp_tree)

	mincost = cost_calc.blabla(nodes,trees[0])
	minpos = 0
	i =0
	for t in trees[1:]:
		i+=1
		c_temp = cost_calc.blabla(nodes,t)
		if(c_temp < mincost):
			mincost = c_temp
			minpos = i
	print("pre eu cost = "+str(mincost))
	a = trees[minpos]

	for e in all_edge:
		v1,v2 = (e.v1,e.v2)
		plot_all_edge.append((v1,v2))

	tot = 0
	for i in range(10):
		start = timeit.default_timer()
		a,b = heu_cut(a,all_edge,nodes)
		stop = timeit.default_timer()
		tot = tot + (stop - start)
		print("cost = " + str(b) + ' time: ' + str(tot))

	print_array(a)
	for e in a:
		v1,v2 = (e.v1,e.v2)
		plot_solution.append((v1,v2))

	toPlot.toPlot(nodes, plot_all_edge, plot_solution)


if(__name__ =='__main__'):
	main()