import sys
sys.path.append("../")
from tabu import tabu
from Edge import Edge_class as Edge
from Util import util
from grasp_kruskal import grasp_kr as gk
import timeit



def main():
	file_name = "../graphs/graph_ppt.txt"
	nodes,temp = util.read(file_name)
	all_edge = []
	for t in temp:
		c,a,b = t.split(" ")
		all_edge.append(Edge.Edge(a,b,c))
	all_edge.sort(key = lambda x: x.cost)
	arr_edge = []
	'''for e in all_edge:
		arr_edge.append(e)
		a,b = util.cic(arr_edge)
		if(a):
			arr_edge.pop()'''
	arr_edge = gk.kruskal(all_edge)

	
	mincost = util.blabla(nodes,arr_edge)
	minarr = arr_edge
	print("pre tabu cost "+str(mincost))
	newcost = mincost
	tabu_list = []
	counter = 0
	tot = 0
	start = timeit.default_timer()
	for i in range(30):
		newarr,newcost = tabu.tabu(arr_edge,all_edge,nodes,tabu_list)
		print("step n "+str(i+1)+" cost = "+str(newcost))
		
		stop = timeit.default_timer()
		tot += stop-start
		print("time = "+str(tot))
		start = timeit.default_timer()
		arr_edge = newarr
		if(newcost >= mincost):
			#util.print_array(tabu_list)
			counter+=1
		else:
			minarr,mincost = util.copy_array(newarr,newcost)
			counter =0
		if(counter == 5):
			break
	print("best cost = "+str(mincost))
	print("time = "+str(tot))
	stop = timeit.default_timer()
	tot += stop-start
	util.print_array(minarr)



if (__name__ == '__main__'):
	main()