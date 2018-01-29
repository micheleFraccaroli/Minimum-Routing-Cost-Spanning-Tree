
class Edge():
	"""docstring for arr_item"""
	
	def __init__(self, a,b,c):
		self.v1 = int(a)
		self.v2 = int(b)
		self.cost = int(c)

	def same(self,e):
		if((self.v1 == e.v1) and (self.v2 == e.v2)):
			return True
		elif ((self.v2 == e.v1) and (self.v1 == e.v2)):
			return True
		else:
			return False

	def toString(self):
		return str(self.v1)+" "+str(self.v2)+" "+str(self.cost)

	def connected_left(self,nodo):
		if(self.v1 == nodo):
			return True
		else:
			return False
	def connected_right(self,nodo):
		if(self.v2 == nodo):
			return True
		else:
			return False
	def cheaper(self,edge):
		if(self.cost < edge.cost):
			return True
		else:
			return False


def sort_edge(e1,e2):
	if(e1.cheaper(e2)):
		return False
	else:
		return True

def cicle(arr_edge):
	arr_nodi = []
	for edge in arr_edge:
		conn1 = False
		conn2 = False
		for nodo in arr_nodi:
			if(edge.connected_left(nodo)):
				conn1 = True
			if(edge.connected_right(nodo)):
				conn2 = True
			if(conn1 and conn2):
				return True
		if(conn1):
			arr_nodi.append(edge.v2)
		if(conn2):
			arr_nodi.append(edge.v1)
		if((conn1 == False) and (conn2 == False)):
			arr_nodi.append(edge.v1)
			arr_nodi.append(edge.v2)
	return False

def cycle(arr_edge):
	if(arr_edge == []):
		return False
	seen = []
	for edge in arr_edge:
		n = edge.v1
		for edge2 in arr_edge:
			if(edge2 == edge):
				continue
			if((edge2.v1 == n) or (edge2.v2 == n))
	


def main():
	try:
		f = open("graph.txt","r")
	except Exception as e:
		print("errore!! "+str(e))
	arr = [];
	temp = f.readline()
	temp = temp[:len(temp)-1]
	n_nodi = int(temp)
	temp = f.readline()
	temp = temp[:len(temp)-1]
	while(temp != ''):
		(a,b,c) = temp.split(" ",3)
		e = Edge(a,b,c)
		arr.append(e)
		temp = f.readline()
		temp = temp[:len(temp)-1]
	tree = []
	#sorting arr
	arr.sort(key = lambda x: x.cost)

	for edge in arr:
		tree.append(edge)
		if(cicle(tree)):
			tree.pop()
	for edge in tree:
		print(edge.toString())
	print("any cicles = "+ str(cicle(arr)))



if(__name__ == '__main__'):
	main()