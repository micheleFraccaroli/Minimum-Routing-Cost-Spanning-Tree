
class Edge():
	"""docstring for arr_item"""
	
	def __init__(self, a,b,c):
		self.v1 = a
		self.v2 = b
		self.cost = int(c)

	def same(self,e):
		if((self.v1 == e.v1) and (self.v2 == e.v2) and (self.cost == e.cost)):
			return True
		elif((self.v2 == e.v1) and (self.v1 == e.v2) and (self.cost == e.cost)):
			return True
		else:
			return False

			
	def same_unstructured(self,v1,v2,c):
		if((self.v1 == v1) and (self.v2 == v2) and self.cost == c):
			return True
		elif((self.v2 == v1) and (self.v1 == v2) and self.cost == c):
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
			return 
	def copy(self):
		e = Edge(self.v1,self.v2,self.cost)
		return e


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


def tour(couple,arr_edge,used):
	a,b = couple
	if(a == b):
		return True
	for edge in arr_edge:
		try:
			used.index(edge)
		except:
			if(edge.connected_right(a)):
				used.append(edge)
				return tour((edge.v1,b),arr_edge,used)
			if(edge.connected_left(a)):
				used.append(edge)
				return tour((edge.v2,b),arr_edge,used)

	return False
		
def print_tree(tree):
	for e in tree:
		print(e.toString())

def cycle(arr_edge):
	for edge in arr_edge:
		a,b = (edge.v1,edge.v2)
		if(tour((a,b),arr_edge,[edge])):

			print("ciclo con "+edge.toString())
			print("albero")
			print_tree(arr_edge)
			print("\n")
			return True
	return False

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
		a,b = cic(tree)
		if(a):
			print("cicle")
			for j in b:
				print(j.toString())
			print("")
			tree.pop()
	print("tree")


	for edge in tree:
		print(edge.toString())
	
	temp = ['1','2','3','4','5','6']
	print("tot = "+str(blabla(temp,tree)))
	#print("any cicles = "+ str(cycle(arr)))

def cic(arr_edge):
	for edge in arr_edge:
		a,b = path_cost(edge.v1,edge.v2,arr_edge,[edge])
		if(a>=0):
			b.append(edge)
			return (True,b)

	return (False,[])


def path_cost(root,node,arr_edge,seen):
	pth =[]
	if(root == node):
		return (0,[])
	for edge in arr_edge:
		try:
			seen.index(edge)
		except:
			if(edge.connected_left(root)):
				seen.append(edge)
				(res,pth) = path_cost(edge.v2,node,arr_edge,seen)
				if(res >=0):
					pth.append(edge)
					return ((res+edge.cost),pth)
				else:
					continue

			elif(edge.connected_right(root)):
				seen.append(edge)
				(res,pth) = path_cost(edge.v1,node,arr_edge,seen)
				if(res >=0):
					pth.append(edge)
					return ((res+edge.cost),pth)
				else:
					continue
	return (-1,[])



def SPT(root, arr_node,arr_edge):
	cost =0
	for node in arr_node:
		if(node == root):
			continue
		a,b =path_cost(root,node,arr_edge,[])
		cost += a

	return cost

def blabla(arr_node,arr_edge):
	cost  =0
	for node in arr_node:
		cost += SPT(node,arr_node,arr_edge)
	return cost


if(__name__ == '__main__'):
	main()