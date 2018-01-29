import sys
sys.path.append("../")
from Edge import Edge_class
from Util import util


MAXLENGTH = 10
def in_list(edge,tabu_list):
	f = False
	for e in tabu_list:
		if(e.same(edge)):
			f = True
			break
	return(f)

def append_to_tabu(edge,tabu_list):
	if(MAXLENGTH ==0):
		return
	if(len(tabu_list) == MAXLENGTH):
		tabu_list.pop(0)
		tabu_list.append(edge)
	else:
		tabu_list.append(edge)

def tabu(arr_edge,all_edge,nodes,tabu_list):
	free_edge = []
	solution_array = []
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
		a,b = util.cic(arr_edge)
		
		for h in b:
			if(h.same(e)):
				continue
			elif(in_list(h,tabu_list)):
				continue
			else:
				util.pop_element(arr_edge,h)
				newmin = util.blabla(nodes,arr_edge)
				x,y = util.copy_array(arr_edge,newmin)
				solution_array.append((x,y,h.copy()))
				arr_edge.append(h)

		util.pop_element(arr_edge,e)

	minarr,mincost,tabuedge = solution_array[0]
	#return((minarr,mincost))
	counter =0
	minpos =0
	for a,c,e in solution_array[1:]:
		counter +=1
		if(c < mincost):
			minpos = counter
			mincost = c
	minarr,mincost,tabuedge = solution_array[minpos]
	append_to_tabu(tabuedge,tabu_list)
	return((minarr,mincost))

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



def tabu2(arr_edge,all_edge,nodes,tabu_list):
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
			a,b = util.copy_array(temp,cost)
			solution_array.append((a,b,c_edge.copy()))
			temp.remove(c_edge)
	
	t_arr,mincost,e_min = solution_array[0]
	minpos = 0
	i=0
	for a,b,e in solution_array[1:]:
		i+=1
		if(b<mincost):
			minpos = i
			mincost = b
	res_arr,res_cost,e_min = solution_array[minpos]
	tabu_list.append(e_min)
	return((res_arr,res_cost))