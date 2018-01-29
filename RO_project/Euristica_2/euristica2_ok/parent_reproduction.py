import sys
import random
import cost_calc as cc
#sys.path.append("../")
#from Util import util


def parent_reproduction(parent1, parent2, nodes):
    res = []
    res.extend(parent1)

    for e2 in parent2:
        found = False
        for e1 in parent1:
            if(e2.same(e1)):
                found = True
                break
        if(not found):
            res.append(e2)

    a, b = cc.cic(res)

    while (a):
        res.sort(key = lambda x: x.cost)
        res.pop(random.randint(len(res)-2, len(res)-1))
        a, b = cc.cic(res)

    return res
