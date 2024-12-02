from random import random as rd
from random import randint as ri

def normlist(l: list[float], ct: int, normalize: bool) -> list[float]:
    return [i/ct for i in l] if normalize else l

#Monte Carlo generate an uniform distribution
def edist(n: int, ct: int, normalize: bool) -> list[float]:
    out = [0 for _ in range(n+1)]
    for _ in range(ct): 
        out[randint(0, n+1)] += 1
    return mornlist(out, ct, normalize)

def gencflip(ph: float):
    return int(rd() >= ph)

# Generate random number according to custom distribution
def gencnum(pdist: list[float]):
    r = rd()
    cumprob = [sum(pdist[1][:i+1]) for i in range(len(pdist[1]))]
    print(cumprob)
    for i, p in enumerate(zip([0] + cumprob, cumprob + [1])):
        if (p[0]<=r) and (r<p[1]): 
            return i

# Monte Carlo generate a custom distribution
def cdist(pdist: list[list[int], list[float]], ct: int, normalize: bool, enumerate: bool) -> list[float]:
    out = [0 for _ in range(len(pdist[0]) + 1)]
    for _ in range(ct):
        out[gencnum(pdist)] += 1
    return normlist(out, ct, normalize) if not enumerate else [*zip(pdist[0], normlist(out, ct, normalize))]

# Monte Carlo generate a repeated uniform distribution (eg n dice)
def repnedist(zeroindex: bool, n: int, reps: int, ct: int, normalize: bool, enum: bool) -> list[float]:
    # 1 ... n * reps -> reps ... reps * n has (n-1) * reps elements
    out = [0 for _ in range((n-1) * reps + 1)]
    for _ in range(ct):
        total = 0
        for _ in range(reps):
            total += ri(1,n)
        out[total-reps] += 1
    return [*zip([*range(reps - zeroindex * reps, reps*n + 1 - zeroindex * reps)], normlist(out, ct, normalize))] if enum else  normlist(out, ct, normalize)

def repncdist(pdist: list[list[int], list[float]], reps: int, ct: int, normalize: bool, enumerate: bool) -> list[float]:
    # output has (len(X) - 1) * reps elements
    out = [0 for _ in range((len(pdist[0]) - 1) * reps)]
    for _ in range(ct):
        total = 0
        for _ in range(reps):
            total += gencnum(pdist)
    return 0 # TO-DO: finish

def getnumfromprompt(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except:
            print("Please enter a valid number.")