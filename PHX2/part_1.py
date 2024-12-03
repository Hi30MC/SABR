import pandas as pd
import sklearn as sk

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