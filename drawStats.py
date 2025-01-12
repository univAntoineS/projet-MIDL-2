import pandas as pd

import matplotlib.pyplot as plt

def drawStats(group):

    Gold = pd.read_csv("data/stats/Gold"+group+".csv")
    Silver = pd.read_csv("data/stats/Silver"+group+".csv")
    Bronze = pd.read_csv("data/stats/Bronze"+group+".csv")


    plt.scatter(Gold[group], Gold['0'],c="y")
    plt.scatter(Silver[group], Silver['0'], c= "#AAAAAA")
    plt.scatter(Bronze[group], Bronze['0'], c="#D95319")
    plt.show()



drawStats("PriorGold")
drawStats("PriorSilver")
drawStats("PriorBronze")
drawStats("NbPriorParticipation")
