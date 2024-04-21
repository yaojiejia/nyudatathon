import pandas as pd
import matplotlib.pyplot as plt

# get data
df = pd.read_csv('sewonkim-test/data.csv')
cols = ["STATEABBRV", "COUNTY", 
    "CFLD_AFREQ", 
    "CFLD_EXPB", "CFLD_EXPP", "CFLD_EXPPE", "CFLD_EXPT", "CFLD_EXP_AREA",
    "CFLD_HLRB", "CFLD_HLRP", "CFLD_HLRR", "CFLD_EALR",
    "CFLD_ALRB", "CFLD_ALRP", "CFLD_ALR_NPCTL",
    "CFLD_RISKV", "CFLD_RISKS", "CFLD_RISKR"]
flooding_df = df[cols]
flooding_df = flooding_df.head(800)

# group by county
group_df = flooding_df[["STATEABBRV", "COUNTY", "CFLD_RISKV"]].groupby(["STATEABBRV", "COUNTY"])
risk_df = group_df.agg("mean")

# plot
risk_df['CFLD_RISKV'].plot(kind='bar')
plt.title('Coastal Flooding Risk of Counties')
plt.xlabel('Index')
plt.xticks(rotation=0, fontsize=5)
plt.ylabel('CFLD_RISKV')
plt.show()