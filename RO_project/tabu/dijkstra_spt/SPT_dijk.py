import dijkstra as dk
import sys
import reading_graph_txt as rd
import random
from random import shuffle
sys.path.append("../")
import Util

MAX = 3

def cost_tree_grasp(nodes, tree):
    cost = Util.blabla(nodes, tree)
    return cost

def grasp(nodes, tree):
    tree_list = []
    cost = cost_tree_grasp(nodes, tree)
    tree_list.append(tree.sort(key = lambda x: cost))

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
    shuffle(list)
    return list[:10]
'''
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
'''