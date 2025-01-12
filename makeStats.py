import pandas as pd 

data = pd.read_csv("data/data.csv",index_col=0)

def saveStats(data,group):
    (data.groupby(group)["Medal"].count()/data.groupby(group)["Name"].count()).sort_values().to_csv("data/stats/Medal"+group+".csv")

    (data[data["Medal"] == "Gold"].groupby(group)["Medal"].count()/data.groupby(group)["Name"].count()).fillna(0).sort_values().to_csv("data/stats/Gold"+group+".csv")
    (data[data["Medal"] == "Silver"].groupby(group)["Medal"].count()/data.groupby(group)["Name"].count()).fillna(0).sort_values().to_csv("data/stats/Silver"+group+".csv")
    (data[data["Medal"] == "Bronze"].groupby(group)["Medal"].count()/data.groupby(group)["Name"].count()).fillna(0).sort_values().to_csv("data/stats/Bronze"+group+".csv")


saveStats(data,"NOC")
saveStats(data,"Age")
saveStats(data,"Height")
saveStats(data,"Weight")
saveStats(data,"Year")
saveStats(data,"PriorGold")
saveStats(data,"PriorSilver")
saveStats(data,"PriorBronze")
saveStats(data,"NbPriorParticipation")
saveStats(data,"is_country_hosting")
saveStats(data,"Sport")
saveStats(data,"Event")
saveStats(data,"PriorGold")
saveStats(data,"PriorSilver")
saveStats(data,"PriorBronze")