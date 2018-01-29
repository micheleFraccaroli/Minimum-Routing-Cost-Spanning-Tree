import SPT_dijk as spt
import reading_graph_txt as rgt
import cost_calcimport sys
sys.path.append("../")
import grasp as gra
import toPlot
import timeit
import signal, os

BEST = 0

def handler(signum, frame):
    print('\n-----------------\nALARM_BEST_COST: ' + str(BEST) + '\n-----------------\n')

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

		for c_edge in c_edges:
			temp.append(c_edge)
			cost = cost_calc.blabla(nodes,temp)

			solution_array.append(copy_array(temp,cost))
			temp.remove(c_edge)
	
	t_arr,mincost = solution_array[0]
	print("mincost_heu = "+str(mincost))
	minpos = 0
	i=0
	for a,b in solution_array[1:]:
		i+=1
		if(b<mincost):
			minpos = i
			mincost = b

	return solution_array[minpos]

def cost_final_solution(nodes, tree):
    cost = cost_calc.blabla(nodes, tree)
    return cost

def main():
	global BEST
	nodes,temp = rgt.read("../../graph/graph_ppt.txt")
	found = False
	signal.signal(signal.SIGALRM, handler)
	all_edge = []
	grasp_tree = []
	best_final = []
	plot_all_edge = []
	plot_solution = []
	counter = 0
	for t in temp:
		c,a,b = t.split(" ")
		e = cost_calc.Edge(a,b,c)
		all_edge.append(e)

	
	gr_start = timeit.default_timer()	
	grasp_tree, d_time = gra.grasp(nodes, temp)
	gr_stop = timeit.default_timer()
	#print('time_GRASP: ' + str(gr_stop - gr_start) + '\n')

	start = timeit.default_timer()
	for gt in grasp_tree:
		print('\n--- MSLS ---')
		print_array(gt)
		print('-------------\n')
		
		time = 0
		j = 0
		signal.setitimer(signal.ITIMER_REAL,100 , 50)
		solution_grasp_i, bb = heu_cut(gt, all_edge, nodes)
		BEST = bb
		print('-------> cost_LS: ' + str(bb))
		best_cost = bb
		best_sol = []
		best_sol.extend(solution_grasp_i)

		for i in range(15):
			solution_grasp_i, bb = heu_cut(solution_grasp_i, all_edge, nodes)
			if(bb < best_cost):
				best_cost = bb
				best_sol = []
				best_sol.extend(solution_grasp_i)
				print('-------> cost_LS: ' + str(best_cost))
			else:
				print("-------> cost_LS: " + str(bb) + "\nStop_LS!\n")
				break
		best_final.append(best_sol)
		stop = timeit.default_timer()
	best_final.sort(key = lambda x: cost_final_solution(nodes, x))
	print('\n--- LS ---\n')
	print_array(best_final[0])
	print('------------')

	print('DIJKSTRA TIME ---> ' + str(d_time))
	print('MSLS TIME    ---> ' + str(gr_stop - gr_start))
	print('LS TIME       ---> ' + str(stop-start))

	for e in all_edge:
		v1, v2 = (e.v1, e.v2)
		plot_all_edge.append((v1,v2))
	for e in best_final[0]:
		v1, v2 = (e.v1, e.v2)
		plot_solution.append((v1,v2))

	toPlot.toPlot(nodes, plot_all_edge, plot_solution)

if(__name__ =='__main__'):
	main()