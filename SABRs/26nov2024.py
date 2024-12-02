from random import random as rn
import util as u

gc = 0
sc = 0

while gc == 0:
    for _ in range(2430):
        count = 0
        for _ in range(27):
            count += 1 - u.gencflip(0.320) # fxn returns P(H), we need P(T) here
        if count == 0:
            gc += 1
    sc += 1
print("took " + str(sc) + " seasons to get perfect game")