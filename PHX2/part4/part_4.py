import pandas as pd

"""
Team: SEA
1. For your assigned team, create a master file by joining the files for the
provided 10 years in the ‘Data Management’ folder for your team only.
2. Next, create:
    a. Top player WAR (higher is better) for each year of the decade (2007-
    2016) for your team
    b. Top 10 player/year combinations (AB > 400) by OPS (higher is better)
    for the decade
"""

# Import CSV files
data_2007 = pd.read_csv("PHX2/part3/data/2007+Bat.csv").fillna(0)
data_2008 = pd.read_csv("PHX2/part3/data/2008+Bat.csv").fillna(0)
data_2009 = pd.read_csv("PHX2/part3/data/2009+Bat.csv").fillna(0)
data_2010 = pd.read_csv("PHX2/part3/data/2010+Bat.csv").fillna(0)
data_2011 = pd.read_csv("PHX2/part3/data/2011+Bat.csv").fillna(0)
data_2012 = pd.read_csv("PHX2/part3/data/2012+Bat.csv").fillna(0)
data_2013 = pd.read_csv("PHX2/part3/data/2013+Bat.csv").fillna(0)
data_2014 = pd.read_csv("PHX2/part3/data/2014+Bat.csv").fillna(0)
data_2015 = pd.read_csv("PHX2/part3/data/2015+Bat.csv").fillna(0)
data_2016 = pd.read_csv("PHX2/part3/data/2016+Bat.csv").fillna(0)
data_list = [data_2007, data_2008, data_2009, data_2010, data_2011, data_2012, data_2013, data_2014, data_2015, data_2016]
cum_data = pd.concat(data_list)

# Part 1: Create team CSV (Tm = SEA)

team_data = cum_data.loc[cum_data["Tm"] == 'SEA']

with pd.ExcelWriter("PHX2/part4/output.xlsx") as writer:
    team_data.to_excel(writer, sheet_name="SEA", index=False)
    
# Part 2: Data Crunching

top_WAR_df = pd.concat([pd.DataFrame([team_data.loc[team_data["Year"] == y].sort_values("WAR/pos", ascending=False).iloc[0][["Year", "Player", "WAR/pos"]]], columns=["Year", "Player", "WAR/pos"], index=[0]) for y in range(2007, 2017)], ignore_index=True)

top_OPS_10 = team_data.loc[team_data["AB"]>400].sort_values("OPS", ascending=False).iloc[:10][["ID", "Player", "Year", "OPS", "AB"]].reset_index(drop=True)

with pd.ExcelWriter("PHX2/part4/output2.xlsx") as writer:
    top_WAR_df.to_excel(writer, sheet_name="Top WAR", index=False)
    top_OPS_10.to_excel(writer, sheet_name="Top OPS Players", index=False)