#get data
with open("SABRs/28jan2025/qbs.csv", "r") as f:
    qbs_pref = [i[:-2:].split(",")[1::] for i in [*f.readlines()]]

with open("SABRs/28jan2025/teams.csv", "r") as f:
    team_pref = [[s for s in i[:-1:].split(",") if s != ""] for i in [*f.readlines()]]

qbs = {j:0 for i in qbs_pref for j in i}
teams = {j:0 for i in team_pref for j in i}

# start getting actual results
for i in qbs_pref[1]:
    qbs[i] += 1

print(max(qbs, key=qbs.get))

print(len(qbs_pref[1]))

qbs = {j:0 for i in qbs_pref for j in i}

for i in [1, 2, 3, 4, 5]:
    for r in qbs_pref[i-1]:
        qbs[r] += 6-i

print(max(qbs, key=qbs.get), qbs["Lamar"])

for j in [i for k in team_pref for i in k]:
    teams[j] += 1

print(teams)

"""
results
1
a) Allen (10)
b) Allen (10)
c) Allen (10)
d) Lamar (86)

2)
             1   2   3
Canditate A: 13, 0,  0
Candidate B: 8, 16, 16
Candidate C: 0,  9,  9

3)
a) won plural but lost total
b) I think that johnson should have won
c) barkley and jordan are in a tie (772 each)
d) dishonest men use the plurality to lie about results, only if you are an honest man you are able to win via his system

4) 
a) chiefs
b) no net effect on either

5) none, makes sense
"""