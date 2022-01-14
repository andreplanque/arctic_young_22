import matplotlib.pyplot as plt
from data import *

def plot_algae(days, algae):
    t = [day.day for day in days]
    if algae == "duna":
        plt.plot(t, [day.duna10.avg() for day in days], "r", label="10% seawater")
        plt.plot(t, [day.duna50.avg() for day in days], "orange", label="50% seawater")
        plt.plot(t, [day.duna100.avg() for day in days], "g", label = "100% seawater")

        plt.errorbar(t, [day.duna100.avg() for day in days], yerr=[day.duna100.err() for day in days], ecolor="g", fmt="none", capsize=2)
        plt.errorbar(t, [day.duna50.avg() for day in days], yerr=[day.duna50.err() for day in days], ecolor="orange", fmt="none", capsize=2)
        plt.errorbar(t, [day.duna10.avg() for day in days], yerr=[day.duna10.err() for day in days], ecolor="r", fmt="none", capsiz=2)

        plt.title("Dunaliella tertiolecta")

    elif algae == "nanno":
        plt.plot(t, [day.nano10.avg() for day in days], "r", label="10% seawater")
        plt.plot(t, [day.nano50.avg() for day in days], "orange", label="50% seawater")
        plt.plot(t, [day.nano100.avg() for day in days], "g", label="100% seawater")

        plt.errorbar(t, [day.nano100.avg() for day in days], yerr=[day.nano100.err() for day in days], ecolor="g", fmt="none", capsize=2)
        plt.errorbar(t, [day.nano50.avg() for day in days], yerr=[day.nano50.err() for day in days], ecolor="orange", fmt="none", capsize=2)
        plt.errorbar(t, [day.nano10.avg() for day in days], yerr=[day.nano10.err() for day in days], ecolor="r", fmt="none", capsize=2)

        plt.title("Nannochloropsis oceanica")

        
    plt.xlabel("Days")
    plt.ylabel(f"Biomass concentration\n{r'($g_{DCW}$ $L^{-1}$)'}")
    plt.ylim([-1, 9])
    plt.legend(loc="upper left")
    plt.savefig(f"{algae}.svg")
    #plt.show()

plot_algae(days, "nanno")