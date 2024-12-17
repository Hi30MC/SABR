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
X1 = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Plate Discipline", usecols = "A,C:N").merge(right=pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Batted Ball Profile", usecols = "A,C:Q"), left_on="TEAM", right_on="TEAM")
WOBA23 = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Statcast Hitting 2023", usecols = "N")
T1 = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Plate Discipline 2023", usecols = "A,C:N").merge(right=pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Batted Ball Profile 2023", usecols = "A,C:Q"), left_on="TEAM", right_on="TEAM")

# Create linear regression models using scikit-learn

# data_set1 = X1[["ZONE CONTACT%", "GB%" , "FB%", "LD%", "PU%", "WEAK%", "TOPPED%", "UNDER%", "FLARE/BURNER%", "SOLID%", "BARREL%"]]
# data_set1 = X1[["ZONE CONTACT%", "GB%" , "FB%", "LD%", "WEAK%", "FLARE/BURNER%", "SOLID%", "BARREL%"]]
# data_set1 = X1[["ZONE CONTACT%", "SOLID%", "BARREL%"]]
data_set1 = X1[["PITCHES", "EDGE%", "BBE", "WEAK%", "TOPPED%", "UNDER%", "FLARE/BURNER%", "SOLID%", "BARREL%"]]

reg1 = sm.OLS(WOBA, data_set1)
model1 = reg1.fit()

# Used to remove columns whose p-values are over 0.05, not needed once these columns are removed

print(model1.pvalues)
print(model1.pvalues.max(numeric_only=True))

# False positives when contracting columns, had to keep going

# T1 = T1[["ZONE CONTACT%", "GB%" , "FB%", "LD%", "PU%", "WEAK%", "TOPPED%", "UNDER%", "FLARE/BURNER%", "SOLID%", "BARREL%"]]
# T1 = T1[["ZONE CONTACT%", "GB%" , "FB%", "LD%", "WEAK%", "FLARE/BURNER%", "SOLID%", "BARREL%"]]
# T1 = T1[["ZONE CONTACT%", "SOLID%", "BARREL%"]]
T1 = T1[["PITCHES", "EDGE%", "BBE", "WEAK%", "TOPPED%", "UNDER%", "FLARE/BURNER%", "SOLID%", "BARREL%"]]

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
print(f"MAE: \n{model1_MAE}") #0.007604
print(model1.summary()) 

"""
AE:
                  WOBA
A's           0.002424
Angels        0.016000
Astros        0.000882
Blue Jays     0.002872
Braves        0.013833
Brewers       0.009844
Cardials      0.000012
Cubs          0.011011
Diamondbacks  0.017617
Dodgers       0.007311
Giants        0.012669
Guardians     0.003015
Mariners      0.000075
Marlins       0.002764
Mets          0.003797
Nationals     0.001628
Orioles       0.011734
Padres        0.006245
Phillies      0.017202
Pirates       0.004526
Rangers       0.015215
Rays          0.024240
Red Sox       0.012333
Reds          0.010394
Rockies       0.003011
Royals        0.005840
Tigers        0.005199
Twins         0.000453
White Sox     0.004571
Yankees       0.001398
"""