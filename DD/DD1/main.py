import pandas as pd
import statsmodels.api as sm

# 1 model RS and RA

train_data = pd.read_excel("DD/DD1/trainp12.xlsx")

reg = sm.OLS(train_data["W"], train_data[["RS", "RA"]])
model = reg.fit()

# print(model.pvalues)
# print(model.summary())
# print(model.params)
# print(model.predict([780, 780]))

"""
p-values:
RS: 3.026x10^-15
RA: 8.77x10^-4

Model:

W = 0.1422RS - 0.0342RA

Adj R^2: 0.993
Much higher than in other models

predicted for 780, 780: 84.187 wins, reasonable
"""

# 2: wins based on salary:

reg2 = sm.OLS(train_data["W"], train_data[["RS", "RA", "SALARY"]])
model2 = reg2.fit()

# print(model2.pvalues)
# print(model2.params)
# print(model2.summary())

"""
exact same, mainly bc salary has 0 effect on performance
"""

#Part 3: model train and create

train_data2 = pd.read_excel("DD/DD1/trainp3.xlsx")

cols = "H 1B 2B 3B HR SO SB BA SLG OPS OBA".split(" ")

reg3 = sm.OLS(train_data2["W"], train_data2[cols])
model3 = reg3.fit()

# print(model3.pvalues)
# print(model3.params)
# print(model3.summary())

test_data = pd.read_excel("DD/DD1/test.xlsx")

with open("DD/DD1/out.csv", "w") as f:
    data = [*model3.predict(test_data[cols])]
    f.write("ID,W\n")
    for i,num in enumerate(data):
        f.write(f"{i},{num}\n")
"""
P values are under .05

model coeffs: 

H        -0.381627
1B        0.725058
2B        0.142599
3B       -0.348572
HR       -0.900712
SO       -0.013407
SB        0.061812
BA    -5261.024417
SLG    1969.093926
OPS    1183.716733
OBA    -785.377193

adj r^2 = 0.987

Some make sense, some don't

bases should be pos, but 3b and hr are neg, same with hits, etc
"""

#4: model other sport

train_data3 = pd.read_excel("DD/DD1/trainp4.xlsx")

reg4 = sm.OLS(train_data3["W"], train_data3[["PS", "PA"]])
model4 = reg4.fit()

print(model4.pvalues)
print(model4.params)
print(model4.summary())


"""
model coeffs:
PS: 0.032
PA: -0.009881

model has a-r^2 of .977, much better than SABR 8
"""