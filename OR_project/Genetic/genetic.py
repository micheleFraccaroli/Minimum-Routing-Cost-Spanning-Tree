from fitness import fitness
from Parent_Reproduction import parent_reproduction as pr
import sys
sys.path.append("../")
import random
from Util import util
from Edge import Edge_class as Edge
from tabu import tabu
from reading_graph import reading_graph_txt as rgt
from grasp_kruskal import grasp_kr as gk
from euristica2 import SPT_dijk as spt

import signal
import timeit

POPULATION = 20
TABU_STEP = 3
BESTCOST=-1
def get_solution_cost(solution):
	a,b = solution
	return b

def print_population(pop):
	for a,c in pop:
		print("cost = "+str(c))


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


def mutate(arr_edge,all_edge,nodes):
	res,c = util.copy_array(arr_edge,0)
	free_edges = get_free_edges(arr_edge,all_edge)
	e = res[random.randint(0,len(res)-1)]
	nodes1 = []
	nodes2 = []
	res.remove(e)
	connected_to(e.v1,res,nodes1)
	connected_to(e.v2,res,nodes2)
	c_edges = cut_edges(nodes1,nodes2,free_edges)
	best = c_edges[0]
	for c_edge in c_edges[1:]:
		if(c_edge.cost < best.cost):
			best = c_edge

	#c_edge = c_edges[random.randint(0,len(c_edges)-1)]
	res.append(best)

	return(res)

def diffs(arr1,arr2):
	counter =len(arr1)
	for a in arr1:
		if(util.edge_in_list(a,arr2)):
			counter-=1

	return counter

def crossover(pop,nodes,all_edge):
	res = []
	pop.sort(key = get_solution_cost)
	res.append(pop[0])
	t1,t2 = res[0]
	for a,c in pop[1:]:
		if(util.same_array(a,t1)):
			pass
		else:
			res.append((a,c))
			break
	for i in range(POPULATION-2):
		t1,t2 = fitness.roulette_wheel(pop)
		p1,c = t1
		p2,c = t2
		arr_temp = pr.parent_reproduction(p1,p2,nodes)
		counter =0
		for a,b in res:
			if(diffs(a,arr_temp)<2):
				#print("mutation")
				if(random.uniform(0,1)>0.5):
					arr_temp = mutate(p1,all_edge,nodes)
				else:
					arr_temp = mutate(p2,all_edge,nodes)

		cost = util.blabla(nodes,arr_temp)
		res.append((arr_temp,cost))
	return res


def generate_population(arr_edge,all_edge,nodes):
	tabu_list = []
	solution_array = []
	startcost = util.blabla(nodes,arr_edge)
	#solution_array.append((arr_edge,startcost))
	temp_list = arr_edge
	for i in range(TABU_STEP):
		temp_list,cost = tabu.tabu2(temp_list,all_edge,nodes,tabu_list)
		solution_array.append((temp_list,cost))
	return solution_array

def merge_for_new_population(better_solutions_tabu,newpopulation):
	res = []
	better_solutions_tabu.sort( key = get_solution_cost)
	for x,y in better_solutions_tabu:
		a,c = newpopulation[len(newpopulation)-1]
		if(y<c):
			newpopulation.pop(len(newpopulation)-1)
			newpopulation.append((x,y))
		else:
			break

def find_best(solutions):
	a,mincost = solutions[0]
	for x,y in solutions[1:]:
		if(y<mincost):
			a = x
			mincost = y
	return((a,mincost))

def first_population(nodes,temp):
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
		cost = util.blabla(nodes,temp_tree)
		trees.append((temp_tree,cost))
	return trees

def handler(signum,frame):
	print("ALARM ACUTAL BEST COST = ",str(BESTCOST))

def find_worst(solutions):
	a,mincost = solutions[0]
	for x,y in solutions[1:]:
		if(y>mincost):
			a = x
			mincost = y
	return((a,mincost))

def main():
	global BESTCOST
	global POPULATION
	signal.signal(signal.SIGALRM, handler)
	nodes,temp = rgt.read("../graphs/graph_ppt2.txt")
	all_edge = []
	for t in temp:
		c,a,b = t.split(" ")
		e = Edge.Edge(a,b,c)
		all_edge.append(e)
	#arr_edge = gk.kruskal(all_edge)
	print("generating population")
	start = timeit.default_timer()
	#signal.setitimer(signal.ITIMER_REAL,10,5)
	solutions = first_population(nodes,temp)
	if(len(solutions)< POPULATION):
		POPULATION = len(solutions)
	else:
		solutions = solutions[:POPULATION]
	print_population(solutions)
	best_solution = find_best(solutions)
	x,y = best_solution
	BESTCOST = y
	print("best solution pre genetic = "+str(y))
	best_in_pop = None
	counter =0
	i =0
	tot =0
	for i in range(100):
		i+=1
		print("iteration = "+str(i))
		newpopulation = crossover(solutions,nodes,all_edge)
		print_population(newpopulation)
		solutions = newpopulation
		newpopulation.sort(key = get_solution_cost)
		x,y = newpopulation[0]
		k,m = newpopulation[POPULATION-1]
		print("last cost = "+str(m))

		if(y< best_solution[1]):
			counter =0
			stop = timeit.default_timer()
			tot += stop -start
			start = timeit.default_timer()
			print("tot = "+str(tot))
			'''
			print("tabu")
			better_solutions_tabu = generate_population(x,all_edge,nodes)
			merge_for_new_population(better_solutions_tabu,newpopulation)
			'''
			best_solution = (x,y)
			stop = timeit.default_timer()
			tot += stop -start
			start = timeit.default_timer()
			print("tot = "+str(tot))
			#print("tabu")
		else:
			counter+=1
		best_in_pop = find_best(newpopulation)
		x,y = best_in_pop
		BESTCOST = y
		print("best new pop cost = "+str(y))
		if(counter > 30):
			break
	stop = timeit.default_timer()
	tot += stop-start
	print("finisced at "+str(tot))



if __name__ == '__main__':
	main()
