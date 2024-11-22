from random import random as rd
from random import randint as ri

def normlist(l: list[float], ct: int) -> list[float]:
    return [i/ct for i in l]

def edist(n: int, ct: int, normalize: bool) -> list[float]:
    out = [0 for _ in range(n+1)]
    for _ in range(ct): 
        out[randint(0, n+1)] += 1
    return mornlist(out, ct) if normalize else out


# Monte Carlo generate an output distribution/prob distribution
def cdist(plist: list[float], ct: int, normalize: bool) -> list[float]:
    out = [0 for _ in range(len(plist) + 1)]
    cumprob = [sum(plist[:i+1]) for i in range(len(plist))]
    # print(cumprob) # debug
    for _ in range(ct):
        r = rd()
        for i, p in enumerate(zip([0] + cumprob, cumprob + [1])):
            if (p[0]<=r) and (r<p[1]):
                out[i] += 1
    return normlist(out, ct) if normalize else out

def getnumfromprompt(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except:
            print("Please enter a valid number.")