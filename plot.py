import matplotlib.pyplot as plt
from data import *

def plot_algae(days, algae):
    t = [day.day for day in days]
    if algae == "duna":
        plt.plot(t, [day.duna10.avg() for day in days], "r", label = "10%")
        plt.errorbar(t, [day.duna10.avg() for day in days], yerr = [day.duna10.err() for day in days], ecolor = "r", fmt = "none", capsize = 2)
        plt.plot(t, [day.duna50.avg() for day in days], "y", label = "50%")
        plt.errorbar(t, [day.duna50.avg() for day in days], yerr = [day.duna50.err() for day in days], ecolor = "y", fmt = "none", capsize = 2)
        plt.plot(t, [day.duna100.avg() for day in days], "g", label = "100%")
        plt.errorbar(t, [day.duna100.avg() for day in days], yerr = [day.duna100.err() for day in days], ecolor = "g", fmt = "none", capsize = 2)
    
        plt.title("Duna")

    elif algae == "nano":
        plt.plot(t, [day.nano10.avg() for day in days], "r", label = "10%")
        plt.errorbar(t, [day.nano10.avg() for day in days], yerr = [day.nano10.err() for day in days], ecolor = "r", fmt = "none", capsize = 2)
        plt.plot(t, [day.nano50.avg() for day in days], "y", label = "50%")
        plt.errorbar(t, [day.nano50.avg() for day in days], yerr = [day.nano50.err() for day in days], ecolor = "y", fmt = "none", capsize = 2)
        plt.plot(t, [day.nano100.avg() for day in days], "g", label = "100%")
        plt.errorbar(t, [day.nano100.avg() for day in days], yerr = [day.nano100.err() for day in days], ecolor = "g", fmt = "none", capsize = 2)
    
        plt.title("Nano")

        
    plt.xlabel("Days")
    plt.ylabel("g/L")
    plt.legend(loc="upper left")
    plt.show()

plot_algae(days, "duna")