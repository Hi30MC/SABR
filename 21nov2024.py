import random
import math

def genDist(pw: float, pl: float) -> list[float]:
    #init outlist
    dist = [0 for i in range(10)]

    #get dist via MP
    for i in range(10000):
        score = 0
        for i in range(3):
            r = random.random()
            score += 3 if r<pw else 1 if r < pl+pw else 0
        dist[score] += 1
    #normalize:
    dist = [i/sum(dist) for i in dist]
    #extra: calc mean, var, std:

    m = sum([i*dist[i] for i in range(len(dist))])
    v = sum([(m - i)**2 * dist[i] for i in range(len(dist))])
    std = v ** 0.5

    #normalize
    return dist, [round(m, 4), round(v,4), round(std,4)]

print(genDist(.41, .41))

print(genDist(.40, .40))
print(genDist(.45, .35))
print(genDist(.50, .30))
print(genDist(.60, .20))
print(genDist(.70, .10))
"""
interesting things
1. distribution shifts in direction of higher %
2. score of 8 is impossible to get
3. mean shifts in direction of higher %
4. variance is about the same for a lot of dists assuming %d is the same
5. std dev is about the same for all
"""