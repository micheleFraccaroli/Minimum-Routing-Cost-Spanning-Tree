import sys
sys.path.append("../")
from Edge import Edge_class
from Util import util


MAXLENGTH = 3

def in_list(edge,tabu_list):
	f = False
	for e in tabu_list:
		if(e.same(edge)):
			f = True
			break
	return(f)

def append_to_tabu(edge,tabu_list):
	if(len(tabu_list) == MAXLENGTH):
		tabu_list.pop(0)
		tabu_list.append(edge)
	else:
		tabu_list.append(edge)

def tabu(arr_edge,all_edge,nodes,tabu_list):
	free_edge = []
	free_edge =[]
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
				x, y = util.copy_array(arr_edge,newmin)
				solution_array.append((x,y,e.copy()))
				arr_edge.append(h)

		util.pop_element(arr_edge,e)

	minarr,mincost,tabuedge = solution_array[0]
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