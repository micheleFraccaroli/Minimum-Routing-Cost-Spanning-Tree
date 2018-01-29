import random
import sys
sys.path.append("../")


from Util import util

def get_solution_cost(solution):
	a,b = solution
	return b


def roulette_wheel(solutions):
	solutions.sort(key = get_solution_cost)
	t, worst_cost = solutions[len(solutions)-1]
	t, best_cost = solutions[0]
	tot =0
	temp_array=[]
	temp_array.append(solutions[0])

	for a,b in solutions[1:]:
		found = False
		for l,m in temp_array:
			if(b>m):
				break
			if(b == m):
				if(util.same_array(l,a)):
					found = True
					break
		if(not found):
			temp_array.append((a,b))

	for a,b in temp_array:
		tot+=((worst_cost)-b)
	fit = []
	for a,b in temp_array:
		fit.append((a,b,((worst_cost-b)/tot)))

	rnd = random.uniform(0,1)
	p1 = None
	for a,c,f in fit:
		if(rnd < f):
			p1 = (a,c)
			break
		else:
			rnd -= f
	same = False
	while(not same):
		rnd = random.uniform(0,1)
		p2 = None
		for a,c,f in fit:
			if(rnd < f):
				p2 = (a,c)
				break
			else:
				rnd -= f
		x,c = p1
		y,c = p2
		same = util.same_array(x,y)
	return p1,p2
