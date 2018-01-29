'''
function for detect cycles into the graph
using the 'Union-find algorithm'
p: parent 
r: rank
v: edge
'''
#import cost_calc
import reading_graph_txt as rgt
import toPlot
import random
import os
import sys
sys.path.append("../")
from grasp_kruskal import grasp_kr as gk
from Util import util
from Edge import Edge_class as Edge

import timeit
def print_all_solution(solutions):
	counter =0
	for arr,cost in solutions:
		counter+=1 
		print("soluzione n "+str(counter)+" costo = "+str(cost))
		util.print_array(arr)


def print_pointer(arr):
	for e in arr:
		print(str(e))


def heuristic(arr_edge,base_cost,all_edge,nodes):
	solution_array = []
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
		a,b = util.cic(arr_edge)
		
		for h in b:
			if(h.same(e)):
				continue
			else:
				util.pop_element(arr_edge,h)
				newmin = util.blabla(nodes,arr_edge)
				solution_array.append(util.copy_array(arr_edge,newmin))
				arr_edge.append(h)

		util.pop_element(arr_edge,e)
	solution_array.append((arr_edge,base_cost))

	z,mincost = solution_array[0]
	minpos = 0
	i=0
	for a,c in solution_array:
		i+=1
		if(mincost > c):
			minpos = i
			z,mincost = a,c

	return((z,mincost))



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
		

def main():
	file_name = "../graphs/graph_ppt.txt"
	nodes,temp = rgt.read(file_name)
	all_edge = []
	for t in temp:
		c,a,b = t.split(" ")
		all_edge.append(Edge.Edge(a,b,c))
	#all_edge.sort(key = lambda x: x.cost)
	arr_edge = []
	arr_edge = gk.kruskal(all_edge)
	
	#arr_edge = gk.grasp(all_edge)
	mincost = util.blabla(nodes,arr_edge)
	print("mincost first solution = "+str(mincost))
	print("first solution")
	util.print_array(arr_edge)
	print("heuristic")
	newcost= mincost
	tot = 0
	final_res,t = util.copy_array(arr_edge,mincost)
	start = timeit.default_timer()
	for i in range(50):
		print(str(i+1)+"/50",end="\r")
		arr_edge,newcost= heuristic(arr_edge,newcost,all_edge,nodes)
		print("step "+str(i+1)+" solution to optimize cost = "+str(newcost))
		stop = timeit.default_timer()
		tot += stop-start
		print("time = "+str(tot))
		start = timeit.default_timer()
		if(mincost> newcost):
			mincost = newcost
			final_res = arr_edge
		elif(mincost == newcost):
			break
	print("result = "+str(mincost))
	util.print_array(arr_edge)
	
	



	'''plot_all_edge = []
	for e in all_edge:
		v1,v2 = (e.v1,e.v2)
		plot_all_edge.append((v1,v2))
	plot_solution = []
	for e in arr_edge:
		v1,v2 = (e.v1,e.v2)
		plot_solution.append((v1,v2))

	toPlot.toPlot(nodes,plot_all_edge,plot_solution)'''

if(__name__ == '__main__'):
	main()