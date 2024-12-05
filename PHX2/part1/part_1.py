import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

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
# print(tnames)

WOBA = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Statcast Hitting", usecols="N")
X1 = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Plate Discipline", usecols = "D:N")
# X2 = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Batted Ball Profile", usecols = "D:Q")
WOBA23 = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Statcast Hitting 2023", usecols = "N")
T1 = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Plate Discipline 2023", usecols = "D:N")
# T2 = pd.read_excel("PHX2/part1/PHX2.xlsx", sheet_name = "Batted Ball Profile 2023", usecols = "D:Q")

# Create linear regression models using scikit-learn

reg1 = linear_model.LinearRegression()
data_set1 = X1[["ZONE%","ZONE SWING%","ZONE CONTACT%","CHASE%","CHASE CONTACT %","EDGE%", "1ST PITCH SWING%", "SWING%","WHIFF%","MEATBALL%", "MEATBALL SWING %"]]
model1 = reg1.fit(data_set1, WOBA)

print("The weights for features in model 1:",model1.coef_)
#    ZONE%	    ZONE SWING%	ZONE CONTACT% CHASE%  CHASE CONTACT %	EDGE%  1ST PITCH SWING%	SWING%	   WHIFF%	   MEATBALL%	MEATBALL SWING %
# [[-0.02810999 -0.02807256 -0.00413438 -0.0331963  -0.00134127 -0.01468608  -0.00141497  0.06137332 -0.00731855  0.00343067  0.00115887]]

# Part 2: Use 2023 data to predict; calc AE and MAE

model1_predicted = pd.DataFrame(model1.predict(T1), columns=["WOBA"])
model1_AE = model1_predicted.sub(WOBA23).abs().set_index(tnames.values)
model1_MAE = model1_AE.mean()

print(model1_AE) #in a multiline below
print(model1_MAE) #0.0126

"""
              WOBA
A's           0.018184
Angels        0.015714
Astros        0.006396
Blue Jays     0.004039
Braves        0.014319
Brewers       0.005276
Cardials      0.010931
Cubs          0.017516
Diamondbacks  0.013943
Dodgers       0.021621
Giants        0.008824
Guardians     0.007251
Mariners      0.005599
Marlins       0.003822
Mets          0.000909
Nationals     0.009229
Orioles       0.015814
Padres        0.023651
Phillies      0.024251
Pirates       0.007666
Rangers       0.011890
Rays          0.023038
Red Sox       0.020396
Reds          0.010105
Rockies       0.013847
Royals        0.012447
Tigers        0.018257
Twins         0.011743
White Sox     0.009901
Yankees       0.013100
"""