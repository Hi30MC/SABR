import pandas as pd
import statsmodels.api as sm

"""
1. For last season (2024) for the entire league (all 30 teams – ie, 30 rows of
data), using team-level data from StatCast from Baseball Savant create a
model estimating the variable wOBA (in the ‘Statcast Hitting’ table) using the
variables in the ‘Plate Discipline’ and ‘Batted Ball Profile’ tables. 

2. Next, apply your model to the 2023 season (change year in upper right
dropdown) to estimate wOBA. Calculate the absolute value of the difference
between the actual values in 2021 and your estimated values for each team.
Take the average of those absolute value differences to determine the Mean
Absolute Error.
"""

#1.1 - Model Creation

# grab data
tnames = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Statcast Hitting", usecols="A").iloc[:,0]

WOBA = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Statcast Hitting", usecols="N")
X1 = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Plate Discipline", usecols = "A,D:N").merge(right=pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Batted Ball Profile", usecols = "A,D:Q"), left_on="TEAM", right_on="TEAM")
WOBA23 = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Statcast Hitting 2023", usecols = "N")
T1 = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Plate Discipline 2023", usecols = "A,D:N").merge(right=pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Batted Ball Profile 2023", usecols = "A,D:Q"), left_on="TEAM", right_on="TEAM")

# Create linear regression models using scikit-learn

# data_set1 = X1[["ZONE CONTACT%", "GB%" , "FB%", "LD%", "PU%", "WEAK%", "TOPPED%", "UNDER%", "FLARE/BURNER%", "SOLID%", "BARREL%"]]
# data_set1 = X1[["ZONE CONTACT%", "GB%" , "FB%", "LD%", "WEAK%", "FLARE/BURNER%", "SOLID%", "BARREL%"]]
data_set1 = X1[["ZONE CONTACT%", "SOLID%", "BARREL%"]]

reg1 = sm.OLS(WOBA, data_set1)
model1 = reg1.fit()

# Used to remove columns whose p-values are over 0.05, not needed once these columns are removed

print(model1.pvalues)
print(model1.pvalues.max(numeric_only=True))

# False positives when contracting columns, had to keep going

# T1 = T1[["ZONE CONTACT%", "GB%" , "FB%", "LD%", "PU%", "WEAK%", "TOPPED%", "UNDER%", "FLARE/BURNER%", "SOLID%", "BARREL%"]]
# T1 = T1[["ZONE CONTACT%", "GB%" , "FB%", "LD%", "WEAK%", "FLARE/BURNER%", "SOLID%", "BARREL%"]]
T1 = T1[["ZONE CONTACT%", "SOLID%", "BARREL%"]]

print("Weights in model 1:\n",model1.params) # below in multiline
"""
Weights in model 1:
ZONE CONTACT%    0.002835
SOLID%           0.003988
BARREL%          0.006645
dtype: float64
"""

# Part 2: Use 2023 data to predict; calc AE and MAE
model1_AE = pd.DataFrame(model1.predict(T1), columns=["WOBA"]).sub(WOBA23).abs().set_index(tnames.values)
model1_MAE = model1_AE.mean()

print(f"AE: \n{model1_AE}") #in a multiline below
print(f"MAE: \n{model1_MAE}") #0.010638
print(model1.summary())

"""
AE:
                  WOBA
A's           0.006862
Angels        0.013688
Astros        0.011593
Blue Jays     0.012550
Braves        0.020004
Brewers       0.007996
Cardials      0.005199
Cubs          0.021869
Diamondbacks  0.008997
Dodgers       0.016260
Giants        0.006272
Guardians     0.008582
Mariners      0.000141
Marlins       0.005113
Mets          0.000122
Nationals     0.006092
Orioles       0.006468
Padres        0.006775
Phillies      0.014121
Pirates       0.003186
Rangers       0.015251
Rays          0.028919
Red Sox       0.014712
Reds          0.022879
Rockies       0.010218
Royals        0.009487
Tigers        0.010795
Twins         0.003296
White Sox     0.008127
Yankees       0.013582
"""