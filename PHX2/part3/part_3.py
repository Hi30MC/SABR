import pandas as pd

"""
1.Create a master file for the AL (Lg=’AL’) and a master file for the NL
(Lg=’NL’) by joining the files for the provided 10 years in the ‘Data
Management’ folder.
2. Using the master files separately, create the following for both leagues
(AL and NL) separately:
    a. Top 10 player/year combinations ranked by WAR (higher is better) for
    the decade (2007-2016) for each league
    b. Top 10 player/year combinations (Age > 30) by WAR (higher is better)
    for the decade (2007-2016) for each league
    c. Sum of WAR by the entire year (ie, total WAR for 2007), then rank the
    10 years by WAR (higher is better)
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

# Part 1

# Combine all data

AL = cum_data.loc[cum_data["Lg"] == "AL"].reset_index(drop=True)
NL = cum_data.loc[cum_data["Lg"] == "NL"].reset_index(drop=True)

with pd.ExcelWriter("PHX2/part3/output.xlsx") as writer:
    AL.to_excel(writer, sheet_name="AL", float_format="%.2f")
    NL.to_excel(writer, sheet_name="NL", float_format="%.2f")
    
# Part 2: Data manip

#sort by WAR/pos
top_WAR_AL = AL.sort_values(by="WAR/pos", inplace=False, ascending=False)
top_WAR_NL = NL.sort_values(by="WAR/pos", inplace=False, ascending=False)

top_WAR_AL_10 = top_WAR_AL.iloc[:10,:].reset_index(drop=True)[["ID", "Player", "WAR/pos", "Year", "Lg", "Age"]]
top_WAR_NL_10 = top_WAR_NL.iloc[:10,:].reset_index(drop=True)[["ID", "Player", "WAR/pos", "Year", "Lg", "Age"]]

top_WAR_AL_10_over_30 = top_WAR_AL.loc[top_WAR_AL["Age"]>30].iloc[:10,:].reset_index(drop=True)[["ID", "Player", "WAR/pos", "Year", "Lg", "Age"]]
top_WAR_NL_10_over_30 = top_WAR_NL.loc[top_WAR_NL["Age"]>30].iloc[:10,:].reset_index(drop=True)[["ID", "Player", "WAR/pos", "Year", "Lg", "Age"]]

WARs = {int(df["Year"][5]) : float(df["WAR/pos"].sum().round(4)) for df in data_list}
WAR_Ranking = pd.DataFrame(WARs, index=[0]).transpose().set_axis(["WAR/pos"], axis=1).sort_values(by="WAR/pos", ascending=False).reset_index(drop=False, names="Year")

blank_line = pd.Series([None])

with pd.ExcelWriter("PHX2/part3/output2.xlsx") as writer:
    pd.concat([top_WAR_AL_10, blank_line, top_WAR_AL_10_over_30, blank_line, top_WAR_NL_10, blank_line, top_WAR_NL_10_over_30]).to_excel(writer, sheet_name= "Top AL and NL Data", index=False)
    WAR_Ranking.to_excel(writer, sheet_name="Year WAR Ranking", index=False)

# Sanity Checkers:
# print(data_2007)
# print(top_WAR_AL.dtypes)
# print(top_WAR_AL)
# print(top_WAR_AL_10_over_30)
# print(NL)

