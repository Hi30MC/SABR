import util as u
from util import getnumfromprompt as gnum
from random import random as r


rarity = [0.0026, 0.0064, 0.032, 0.1598, 0.7992] #blue 79.92., purple 15.98, pink 3.2, red .64, gold .26
colors = ["gold", "red", "pink", "purple", "blue"]

# get num cases to open
ct = gnum("Number of cases to open: ")

colordist = [*zip(u.cdist(rarity, ct, False), colors)]

# print count of each color
print(colordist)

# gen list of outputs, print first 5 in order of dec rarity

npc = gnum("Number of each color to display: ")
for i in colordist:
    out = []
    for _ in range(min(i[0], npc)):
        out.append((i[1], round(r(), 2)))
    print(i[1], ":", out)
