class Edge():
	"""docstring for arr_item"""
	
	def __init__(self, a,b,c):
		self.v1 = a
		self.v2 = b
		self.cost = int(c)

	def same(self,e):
		if((self.v1 == e.v1) and (self.v2 == e.v2) and (self.cost == e.cost)):
			return True
		elif((self.v1 == e.v2) and (self.v2 == e.v1) and (self.cost == e.cost)):
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
