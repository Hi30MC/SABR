from random import random as rd
from random import randint as ri

# Normalize a list based on the count of items in the list, if the "normalize" param is True, else do nothing
def normlist(l: list[float], ct: int, normalize: bool) -> list[float]:
    return [i/ct for i in l] if normalize else l

# Calculate the cumulative distribution of a given probability distribution
def cumdist(l: list[float]) -> list[float]:
    out = [0]
    for p in l:
        out.append(out[-1] + p)
    out = [round(i,10) for i in out]
    return out[1:] + [1] if out[-1] != 1 else out[1:]

# Return the outcome of a weighted coin flip
def gencflip(ph: float) -> int:
    return int(rd() >= ph)

# Generate random number according to custom distribution
def gencnum(pdist: list[list[int], list[float]]) -> int:
    r = rd()
    cumprob = cumdist(pdist[1])
    # print(cumprob)
    for i, p in enumerate(zip([0] + cumprob, cumprob + [1])):
        if (p[0]<=r) and (r<p[1]): 
            return i
        
# Generate all possible outputs after n consecutive repetitions of a given distribution
def genpossouts(pdist: list[list[int], list[float]], reps: int) -> list[int]:
    out = set(pdist[0]) #first iteration of process, thus repeat the main code reps-1 times
    for _ in range(reps-1):
        t = set()
        for i in pdist[0]:
            for j in out:
                t.add(i+j)
        out = t
    return out

# Generate probabilty distribution of n consecutive repetitions of a given distribution
def genposspdist(pdist: list[list[int], list[float]], reps:int) -> list[list[int], list[float]]:
    temp = dict(zip(*pdist)) #first iteration of process, thus repeat the main code reps-1 times
    out = dict(temp)
    for _ in range(reps-1):
        t = dict()
        for k1, v1 in temp.items():
            for k2, v2 in out.items():
                t[k1+k2] = t.get(k1+k2, 0) + v1 * v2
        out = t
    return [[*out.keys()], [round(i, 10) for i in out.values()]]

#Monte Carlo generate an uniform distribution (eg. fair dice)
def edist(zeroindex: bool, n: int, ct: int, normalize: bool, enum: bool) -> list[float]:
    out = [0 for _ in range(n)]
    for _ in range(ct): 
        out[ri(0, n-1)] += 1
    out = normlist(out, ct, normalize)
    return [*zip([*range(zeroindex, n+zeroindex)], out)] if enum else out

# Monte Carlo generate a custom distribution (eg. weighted dice)
def cdist(pdist: list[list[int], list[float]], ct: int, normalize: bool, enum: bool) -> list[float]:
    out = [0 for _ in range(len(pdist[0]) + 1)]
    for _ in range(ct):
        out[gencnum(pdist)] += 1
    return normlist(out, ct, normalize) if not enum else [*zip(pdist[0], normlist(out, ct, normalize))]

# Monte Carlo generate a repeated uniform distribution (eg. n fair dice)
def repnedist(zeroindex: bool, n: int, reps: int, ct: int, normalize: bool, enum: bool) -> list[float]:
    if reps == 1:
        return edist(zeroindex, n, ct, normalize, enum)
    # 1 ... n * reps -> reps ... reps * n has (n-1) * reps elements
    out = [0 for _ in range((n-1) * reps + 1)]
    # O((n + ct) * reps)
    for _ in range(ct):
        total = 0
        for _ in range(reps):
            total += ri(1,n)
        out[total-reps] += 1
    return [*zip([*range(reps - zeroindex * reps, reps*n + 1 - zeroindex * reps)], normlist(out, ct, normalize))] if enum else  normlist(out, ct, normalize)

# Monte Calro generate a repeated custom distribution (eg. n weighted dice)
def repncdist(pdist: list[list[int], list[float]], reps: int, ct: int, normalize: bool, enum: bool) -> list[float]:
    tdist = genposspdist(pdist, reps)
    for _ in range(ct):
        return 0

def getnumfromprompt(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except:
            print("Please enter a valid number.")