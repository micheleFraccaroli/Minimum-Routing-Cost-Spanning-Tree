'''
#TABU SEARCH

tabu_list = []
a,C = tabu.tabu(grasp_tree, all_edge, nodes, tabu_list)
print("#####   PRIMA TABU   #####")
print_array(a)
print(C)
print('##########################')

for i in range(500):
	a,c = tabu.tabu(grasp_tree, all_edge, nodes, tabu_list)
	if (c < C):
		C = c
		counter = 0
		print_array(a)
		print(c)
	else:
		counter += 1
	if(counter == 15):
		print('STOP criteria raggiunto' + '\n' + "--- Pre_heuristic(Dijkstra) cost: " + str(mincost)
			+ '\n' + "--- Tabù Search cost: " + str(C))
		break
'''