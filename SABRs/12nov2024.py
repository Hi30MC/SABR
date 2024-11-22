import random
import util as u

#Part 1
print("1.1: Chance of heads: " + u.edist(2, 1000, true))

for i in range(1000):
    counts[random.randint(0,1)+random.randint(0,1)] += 1

print("1.2: Distribution: " + cdist(0,0,0)) # one tail one head most likely b/c there are two ways to get the outcome (HT or TH)

counts = [0 for i in range(6)]

for i in range(1000):
    counts[random.randint(0,5)] += 1

print("1.3: Distribution of a dice roll: " + str([i/1000 for i in counts]))

counts = [0 for i in range(11)]

for i in range(1000):
    counts[random.randint(0,5)+random.randint(0,5)] += 1

print("1.4: Distribution of a double dice roll: " + str([i/1000 for i in counts])) # 7 most likely b/c most amount of pairs that result in 7

# part 2
"""
team: PHI (7-2, record % is 77.8% win, 22.2% loss)
remaining games:
Dallas: 3-6 (33.3% win, 66.7% loss)
WASH: 7-3 (70% win, 30% loss)
LA: 4-5 (44.4% win, 55.6% loss)
Baltimore: 7-3 (70% win, 30% loss)
CAR: 3-7 (30% win, 70% loss)
PIT: 7-2 (77.8% win, 22.2% loss)
WASH: 7-3 (70% win, 30% loss)
Dallas: 3-6 (33.3% win, 66.7% loss)
NYG: 2-8 (20% win, 80%  loss)
"""

def calcWinPercent(a: float, b: float) -> float:
    return (a + (1-b))/2

percents = [calcWinPercent(77.8, 33.3), calcWinPercent(77.8, 70), calcWinPercent(77.8, 44.4), calcWinPercent(77.8, 70)]
percents += [calcWinPercent(77.8, 30), calcWinPercent(77.8, 77.8), calcWinPercent(77.8, 70), calcWinPercent(77.8, 33.3), calcWinPercent(77.8, 20)]
percents = [i/100 for i in percents]

counts = [0 for i in range(len(percents))]

for n in range(50000):
    wins = 0
    for i in range(len(percents)):
        if random.random() >= percents[i]:
            wins += 1
    counts[wins-1] += 1    

print("2.1: Distribution of wins: " + str([i/50000 for i in counts]))
print("2.2: Chance team makes cutoff: " + str(sum(counts[2:])/50000))