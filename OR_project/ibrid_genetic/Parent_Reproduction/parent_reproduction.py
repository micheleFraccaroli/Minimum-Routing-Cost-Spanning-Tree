import sys
import random
sys.path.append("../")
from Util import util

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

    a, b = util.cic(res)
    while (a):
        b.sort(key = lambda x: x.cost)
        if(len(b)>2):
            el = b[random.randint(len(b)-3, len(b)-1)]
        elif(len(b)==2):
            el = b[random.randint(len(b)-2, len(b)-1)]
        else:
            el = b[0]
        util.pop_element(res,el)
        a, b = util.cic(res)

    return res
