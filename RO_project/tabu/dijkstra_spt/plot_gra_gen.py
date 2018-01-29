import sys
import reading_graph_txt as rgt
import cost_calc
sys.path.append("../")
import toPlot

nodes,temp = rgt.read("../../graph/graph_ppt.txt")
all_edge = []
plot_all_edge = []
plot_solution = []
for t in temp:
	c,a,b = t.split(" ")
	e = cost_calc.Edge(a,b,c)
	all_edge.append(e)

for e in all_edge:
	v1, v2 = (e.v1, e.v2)
	plot_all_edge.append((v1,v2))

toPlot.toPlot(nodes, plot_all_edge, plot_solution)