def print_array(arr):
	for e in arr:
		print(e.toString())

def copy_array(arr_edge,cost):
	res = []
	for e in arr_edge:
		res.append(e.copy())
	return (res,cost)


def pop_element(arr,e):
	for i in range(len(arr)):
		if(arr[i].same(e)):
			try:
				arr.pop(i)
				break
			except:
				print("len = "+str(len(arr))+" i = "+str(i))

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
		if(edge_in_list(edge,seen)):
			pass
		else:
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

def read(file):
	try:
		f = open(file,"r")
		r1 = f.readline()
		n = r1[0:len(r1)-1]
		nodes = n.split(",")

		edges = []
		r2 = f.readline()
		n2 = r2[:len(r2)-1]
		#edges.append(n2)
		while(r2 != ''):
			if(r2[len(r2)-1] == '\n'):
				n2 = r2[:len(r2)-1]
			else:
				n2 = r2
			edges.append(n2)
			r2 = f.readline()
		f.close()
		return nodes, edges
	except:
		print("error read file")
		exit()
	
def in_list(el,arr):
	found = False
	for a in arr:
		if(a == el):
			found = True
			break
	return found

def edge_in_list(edge,arr_edge):
	found = False
	for a in arr_edge:
		if(a.same(edge)):
			found = True
			break
	return found

def same_array(arr1,arr2):
	ok = True
	for a1 in arr1:
		if(edge_in_list(a1,arr2)):
			pass
		else:
			ok = False
			break
	return ok