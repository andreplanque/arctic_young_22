import numpy as np
import matplotlib.pyplot as plt
from data import days

def biomass(days, algae):
    avg  = eval(f"[day.{algae}.avg() for day in days]")
    return (max(avg)-min(avg)) / len(days)
    
def bar(days):
    duna = [biomass(days, algae) for algae in ["duna10", "duna50", "duna100"]]
    nanno = [biomass(days, algae) for algae in ["nanno10", "nanno50", "nanno100"]]
    index = np.arange(3)
    width = 0.35
    plt.bar(index, duna, width, label="Duna")
    plt.bar(index + width, nanno, width,  label="Nanno")
    plt.xticks(index + width/2, ("10%", "50%", "100%"))
    plt.title("Biomass productivity")
    plt.ylabel(f"Biomass productivity\n{r'($g_{DCW}$ $L^{-1}$ $days^{-1}$)'}")
    plt.legend(loc="upper left")
    #plt.savefig("biomass.svg")
    plt.show()

bar(days)
