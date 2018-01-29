from collections import defaultdict, deque
import reading_graph_txt as rd
import cost_calc as cc

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial, flag):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                if(flag == False):
                    weight = current_weight + graph.distances[(edge, min_node)]
                else:
                    continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

def shortest_path(graph, origin, destination, flag):
    visited, paths = dijkstra(graph, origin, flag)
    list = []
    temp = []
    path = []
    full_path = deque()
    _destination = paths[destination]
    tuple = (_destination, destination)
    list.append(tuple)
    a = visited[tuple[0]]
    b = visited[tuple[1]]
    w = int(b-a)
    ed = cc.Edge(tuple[0], tuple[1], w)
    path.append(ed)
    temp.append(ed.toString())

    while _destination != origin:
        full_path.appendleft(_destination)
        tmp = _destination
        _destination = paths[_destination]
        tuple = (_destination, tmp)
        list.append(tuple)
        a = visited[tuple[0]]
        b = visited[tuple[1]]
        w = int(b-a)
        ed = cc.Edge(tuple[0],tuple[1],w)
        path.append(ed)
        temp.append(ed.toString())

    temp.reverse()

    return visited[destination], path

'''
if __name__ == '__main__':
    graph = Graph()
    nodes = []
    edges = []
    flag = False
    nodes, edges = rd.read('graph_1.txt')
    #tedg = tuple(edges)

    for node in nodes:
        graph.add_node(node)

    for edge in edges:
        c, v1, v2 = edge.split(" ")
        graph.add_edge(str(v1), str(v2), int(c))

    cost, path =shortest_path(graph, 'A', 'F', flag)
    visited, p = dijkstra(graph, 'A', flag)

    #print(str(visited) + '\n' + str(p))

    print(str(cost) + '\n' + str(path) + '\n')
'''