import dijkstra as dk
import os
import reading_graph_txt as rd

def tree_dijk(root, nodes, edges):
    flag = False
    graph = dk.Graph()
    list = []

    for node in nodes:
        graph.add_node(node)

    for edge in edges:
        c, v1, v2 = edge.split(" ")
        graph.add_edge(str(v1), str(v2), int(c))

    for i in nodes:
        if(i != root):
            cost, path = dk.shortest_path(graph, root, i, flag)
            list.append(path)
    return list

def loop_root_SPT(nodes, edges):
    list = []
    for i in nodes:
        list.append(tree_dijk(i, nodes, edges))
    
    return list


if __name__ == '__main__':
    list = []
    list2 = []
    nodes = []
    edges = []

    nodes, edges = rd.read('graph_1.txt')

    list = tree_dijk('B', nodes, edges)
    list2 = loop_root_SPT(nodes, edges)

    print(list)
    print('\n')
    print(list2)
