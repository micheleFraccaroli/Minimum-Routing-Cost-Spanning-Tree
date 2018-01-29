import random
import sys
sys.path.append("../")
from Util import util


RNJESUS = 3

def kruskal(all_edge):
	res = []
	all_edge.sort(key = lambda x: x.cost)
	for e in all_edge:
		res.append(e)
		a,b = util.cic(res)
		if(a):
			res.pop()
	return res



def grasp(all_edge):
	temp_arr,useless = util.copy_array(all_edge,0)
	res = []
	temp_arr.sort(key = lambda x: x.cost)
	while (True):
		if(0 == (len(temp_arr)-2)):
			element = temp_arr[random.randint(0,1)]
		elif(0== (len(temp_arr)-1)):
			element = temp_arr[0]
		else:
			element = temp_arr[random.randint(0,(RNJESUS-1))]
		util.pop_element(temp_arr,element)
		res.append(element)
		a,b = util.cic(res)
		if(a):
			res.pop()
		if(len(temp_arr)==0):
			break

	return res