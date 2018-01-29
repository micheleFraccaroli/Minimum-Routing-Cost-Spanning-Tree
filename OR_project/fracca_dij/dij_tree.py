import os
import SPT_dijk as spt
import reading_graph_txt as rgt
import sys
sys.path.append("../")
from Util import util
from Edge import Edge_class as Edge
#import cost_calc




def connected_to(node,arr_edge,visited):
	if(not util.in_list(node,visited)):
		visited.append(node)
	for e in arr_edge:
		if(e.connected_left(node)):
			if(not util.in_list(e.v2,visited)):
				connected_to(e.v2,arr_edge,visited)
		if(e.connected_right(node)):
			if(not util.in_list(e.v1,visited)):
				connected_to(e.v1,arr_edge,visited)


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
	arr_edge_cost = util.blabla(nodes,arr_edge)
	#solution_array.append((arr_edge,arr_edge_cost))
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
		for c_edge in c_edges:
			temp.append(c_edge)
			cost = util.blabla(nodes,temp)

			solution_array.append(util.copy_array(temp,cost))
			temp.remove(c_edge)
	
	t_arr,mincost = solution_array[0]
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
	nodes,temp = rgt.read("../graphs/graph_2.txt")
	all_edge = []
	for t in temp:
		c,a,b = t.split(" ")
		e = Edge.Edge(a,b,c)
		all_edge.append(e)
	list_of_list_of_list =spt.loop_root_SPT(nodes,temp)
	trees = []
	for list_of_list in list_of_list_of_list:
		temp_tree = []
		for lis in list_of_list:
			for ed in lis:
				if(util.edge_in_list(ed,temp_tree)):
					pass
				else:
					temp_tree.append(ed)
		trees.append(temp_tree)



	mincost = util.blabla(nodes,trees[0])
	minpos = 0
	i =0
	for t in trees[1:]:
		i+=1
		c_temp = util.blabla(nodes,t)
		if(c_temp < mincost):
			mincost = c_temp
			minpos = i
	print("pre eu cost = "+str(mincost))
	a = trees[minpos]
	mincost = util.blabla(nodes,a)
	for i in range(10):
		a,b = heu_cut(a,all_edge,nodes)
		print("cost = "+str(b))
		if(b<mincost):
			mincost = b
		elif(b == mincost):
			break
	util.print_array(a)


	#dijkstra






if(__name__ =='__main__'):
	main()