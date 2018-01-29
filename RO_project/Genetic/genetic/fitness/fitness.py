import random
import sys
sys.path.append("../../")
from Util import util


def fitness(solutions):
	solutions.sort(key = lambda a,b: b)
	t, worst_cost = solutions[len(solutions)-1]
	t, best_cost = solutions[0]
	tot =0
	for a,b in solutions:
		tot+=b
	fit = []
	for a,b in solutions:
		fit.append(a,b,(worst_cost-b)/tot)

	rnd = random.uniform(0,1)
	p1 = None
	for a,c,f in fit:
		if(rnd < f):
			p1 = (a,c)
			break
		else:
			rnd -= f
	ok = False
	while(not ok):
		rnd = random.uniform(0,1)
		p2 = None
		for a,c,f in fit:
			if(rnd < f):
				p2 = (a,c)
				break
			else:
				rnd -= f
		ok = util.same_array(p1,p2)
	return p1,p2

