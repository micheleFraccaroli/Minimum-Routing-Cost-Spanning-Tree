def print_array(arr):
	for e in arr:
		print(e.toString())

def copy_array(arr_edge,cost):
	res = []
	for e in arr_edge:
		res.append(e.copy())
	return (res,cost)


def pop_element(arr,e):
	for i in range(len(arr)-1):
		if(arr[i].same(e)):
			try:
				arr.pop(i)
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

