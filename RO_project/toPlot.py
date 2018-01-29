import networkx as nx
import matplotlib.pyplot as plt

def toPlot(nodes, edges, sol_edges):
	dict = {}
	G = nx.Graph()
	G.add_nodes_from(nodes)
	pos=nx.spring_layout(G)

	for i in edges:
		trovato = False
		for k in sol_edges:
			if(i == k):
				v1, v2 = i
				G.add_edge(v1,v2, color='r',weight=6)
				trovato = True
		if(not trovato):
			v1, v2 = i
			G.add_edge(v1,v2, color='g', weight=2)
	
	edges = G.edges()
	colors = [G[u][v]['color'] for u,v in edges]
	weights = [G[u][v]['weight'] for u,v in edges]

	nx.draw(G, pos, edges=edges, edge_color=colors, width=weights,with_labels=True, node_color='b', node_size=400, font_size=10, font_color='w')

	nx.draw_networkx_edge_labels(G,pos, dict, clip_on=True)

	plt.savefig("solution.png")
	#plt.show()

nodes = ['A','B','C','D','E','F']
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'E'), ('C', 'D'), ('E', 'D'), ('D', 'F'), ('E', 'F')]
sol = [('A', 'B'), ('A', 'C'), ('B', 'C')]
toPlot(nodes, edges, sol)


