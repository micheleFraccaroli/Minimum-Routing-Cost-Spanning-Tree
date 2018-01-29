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
		while (r2 != ''):
			if (r2[len(r2) - 1] == '\n'):
				n2 = r2[:len(r2) - 1]
			else:
				n2 = r2[:len(r2)]
			edges.append(n2)
			r2 = f.readline()
		f.close()
		return nodes, edges
	except:
		print("error read file")
		exit()
	


'''
nodes = []
list = []
nodes, list = read('graph_1.txt')
print(str(nodes) + '\n' + str(list) + '\n')


'''