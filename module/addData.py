import numpy as np
import pandas as pd

#

#print(data.describe())

def addThisYearParticipation(data) :
    ct = data.groupby(["ID","Year"]).size().reset_index(name='thisYearParticipation')
    return pd.merge(data, ct, how="left", on=["ID","Year"])

def addNbPriorParticipation(data) :
    # pas opti + ne pas utiliser (utiliser addAll)

    group = data.groupby(["ID","Year"])
    df = pd.DataFrame(columns=["ID","Year","NbPriorParticipation"])
    for row in group:
        df.loc[len(df)] = [row[0][0],row[0][1], (row[0][1] > data[data["ID"]==row[0][0]]["Year"]).sum()]
    return pd.merge(data, df, how="left", on=["ID","Year"])

def addPriorGold(data):
    # pas opti + ne pas utiliser (utiliser addAll)
    GoldData = data[data["Medal"] == "Gold"]
    group = data.groupby(["ID","Year"])
    df = pd.DataFrame(columns=["ID","Year","PriorGold"])

    for row in group:
        df.loc[len(df)] = [row[0][0],row[0][1], (row[0][1] > GoldData[GoldData["ID"]==row[0][0]]["Year"]).sum()]
    return pd.merge(data, df, how="left", on=["ID","Year"])

def addPriorSilver(data):
    # pas opti + ne pas utiliser (utiliser addAll)
    SilverData = data[data["Medal"] == "Silver"]
    group = data.groupby(["ID","Year"])
    df = pd.DataFrame(columns=["ID","Year","PriorSilver"])

    for row in group:
        df.loc[len(df)] = [row[0][0],row[0][1], (row[0][1] > SilverData[SilverData["ID"]==row[0][0]]["Year"]).sum()]
    return pd.merge(data, df, how="left", on=["ID","Year"])

def addPriorBronze(data):
    # pas opti + ne pas utiliser (utiliser addAll)
    BronzeData = data[data["Medal"] == "Bronze"]
    group = data.groupby(["ID","Year"])
    df = pd.DataFrame(columns=["ID","Year","PriorBronze"])

    for row in group:
        df.loc[len(df)] = [row[0][0],row[0][1], (row[0][1] > BronzeData[BronzeData["ID"]==row[0][0]]["Year"]).sum()]
    return pd.merge(data, df, how="left", on=["ID","Year"])



def host_country(col):
    if col == "Rio de Janeiro":
        return "BRA"
    elif col == "London":
        return "GBR"
    elif col == "Beijing":
        return  "HKG"
    elif col == "Athina":
        return  "GRE"
    elif col == "Sydney" or col == "Melbourne":
        return  "AUS"  # "ANZ"
    elif col == "Atlanta" or col == "Los Angeles" or col == "St. Louis" or col == "Salt Lake City" or col == "Squaw Valley":
        return  "USA"
    elif col == "Barcelona":
        return  "ESP"
    elif col == "Seoul":
        return  "KOR"
    elif col == "Moskva" or col == "Sochi":
        return  "RUS" # "EUN"
    elif col == "Montreal" or col =="Calgary" or col == "Vancouver":
        return  "CAN"
    elif col == "Munich" or col == "Berlin" or col == "Garmisch-Partenkirchen":
        return  "GER"  # "GDR"
    elif col == "Mexico City":
        return  "MEX"
    elif col == "Tokyo" or col == "Nagano" or col == "Sapporo":
        return  "JPN"
    elif col == "Roma" or col == "Torino" or col == "Cortina d'Ampezzo":
        return  "ITA"
    elif col == "Paris" or col == "Albertville" or col == "Grenoble" or col == "Chamonix":
        return  "FRA"
    elif col == "Helsinki":
        return  "FIN"
    elif col == "Amsterdam":
        return  "NED" # "AHO"?
    elif col == "Antwerpen":
        return  "BEL"
    elif col == "Stockholm":
        return  "SWE"
    elif col == "Lillehammer" or col == "Oslo":
        return "NOR"
    elif col == "Lake Placid" or col == "Innsbruck":
        return "AUT"
    elif col == "Sarajevo":
        return "BIH"
    elif col == "Sankt Moritz":
        return "SUI"
    else:
        return "Other"


def addIsCountryHosting(data):
    data['Host_Country_NOC'] = data['City'].apply(host_country)
    data['is_country_hosting'] = data["Host_Country_NOC"]==data["NOC"]
    return data.drop(columns="Host_Country_NOC")

def addMedalPercentForAttribut(data,Attribut):
    group = data.groupby([Attribut,"Year"])

    priorGoldPercentForGroup = pd.DataFrame(columns=[Attribut,"Year","priorGoldPercentFor" + Attribut])
    priorSilverPercentForGroup = pd.DataFrame(columns=[Attribut,"Year","priorSilverPercentFor" + Attribut])
    priorBronzePercentForGroup = pd.DataFrame(columns=[Attribut,"Year","priorBronzePercentFor" + Attribut])


    i = 0
    for row in group:
        if i%100 == 0:
            print(i , " / ", group.ngroups, " | ", i/group.ngroups , " %")
        i+=1


        athltesBeforeByAttribut = data[(row[0][1] > data["Year"]) & (data[Attribut]==row[0][0])]
        athltesBeforeByAttributSum = (athltesBeforeByAttribut["Year"]).sum()

        if athltesBeforeByAttributSum == 0:
            athltesBeforeByAttributSum = 1
            if athltesBeforeByAttribut.size != 0:
                raise ValueError("should not be possible")

        priorGoldPercentForGroup.loc[len(priorGoldPercentForGroup)] = [row[0][0],row[0][1], 
                                                                   athltesBeforeByAttribut[athltesBeforeByAttribut["Medal"] == "Gold"].size
                                                                   /athltesBeforeByAttributSum]
        priorSilverPercentForGroup.loc[len(priorSilverPercentForGroup)] = [row[0][0],row[0][1], 
                                                                   athltesBeforeByAttribut[athltesBeforeByAttribut["Medal"] == "Silver"].size
                                                                   /athltesBeforeByAttributSum]
        priorBronzePercentForGroup.loc[len(priorBronzePercentForGroup)] = [row[0][0],row[0][1], 
                                                                   athltesBeforeByAttribut[athltesBeforeByAttribut["Medal"] == "Bronze"].size
                                                                   /athltesBeforeByAttributSum]

    merged = pd.merge(data, priorGoldPercentForGroup, how="left", on=[Attribut,"Year"])
    merged = pd.merge(merged, priorSilverPercentForGroup, how="left", on=[Attribut,"Year"])
    merged = pd.merge(merged, priorBronzePercentForGroup, how="left", on=[Attribut,"Year"])

    return merged

def addAll(data,Attributs = ["NOC"]):


    group = data.groupby(["ID","Year"])

    priorParticipation = pd.DataFrame(columns=["ID","Year","NbPriorParticipation"])


    priorGold = pd.DataFrame(columns=["ID","Year","PriorGold"])
    priorSilver = pd.DataFrame(columns=["ID","Year","PriorSilver"])
    priorBronze = pd.DataFrame(columns=["ID","Year","PriorBronze"])

    GoldData = data[data["Medal"] == "Gold"]
    SilverData = data[data["Medal"] == "Silver"]
    BronzeData = data[data["Medal"] == "Bronze"]


    i = 0
    for row in group:
        if i%1000 == 0:
            print(i , " / ", group.ngroups, " | ", i/group.ngroups , " %")
        i+=1

        priorParticipation.loc[len(priorParticipation)] = [row[0][0],row[0][1], (row[0][1] > data[data["ID"]==row[0][0]]["Year"]).sum()]

        priorGold.loc[len(priorGold)] = [row[0][0],row[0][1], (row[0][1] > GoldData[GoldData["ID"]==row[0][0]]["Year"]).sum()] 
        priorSilver.loc[len(priorSilver)] = [row[0][0],row[0][1], (row[0][1] > SilverData[SilverData["ID"]==row[0][0]]["Year"]).sum()]
        priorBronze.loc[len(priorBronze)] = [row[0][0],row[0][1], (row[0][1] > BronzeData[BronzeData["ID"]==row[0][0]]["Year"]).sum()]
    

    merged = pd.merge(data, priorParticipation, how="left", on=["ID","Year"])

    merged = pd.merge(merged, priorGold, how="left", on=["ID","Year"])
    merged = pd.merge(merged, priorSilver, how="left", on=["ID","Year"])
    merged = pd.merge(merged, priorBronze, how="left", on=["ID","Year"])


    merged["Sex"] = merged["Sex"] == "M"

    merged = addIsCountryHosting(addThisYearParticipation(merged))

    for attrib in Attributs:
        merged = addMedalPercentForAttribut(merged,attrib)

    return merged

#newData = addAll(data)
#newData.to_csv("data/data.csv")

# data = pd.read_csv('data/data.csv')

# print(data)
# data = addMedalPercentForAttribut(data,"Event")
# print(data)
# data.to_csv("foo.csv",index = False)

