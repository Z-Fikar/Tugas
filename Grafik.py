# -*- coding: utf-8 -*-


from Simulasi import Simulation
import matplotlib.pyplot as plt

number_of_trials = 100

def generate():
    s = Simulation(trials=number_of_trials)
    for x in range(1000):
        switch_list.append(s.start(switch=True, info=False))
        not_switch_list.append(s.start(switch=False, info=False))

def show():
    plt.ylim(0,100)
    plt.xlim(0,1200)

    plt.plot([x+1 for x in range(len(switch_list))],switch_list, label="Switching", color="purple")
    plt.plot([x+1 for x in range(len(not_switch_list))],not_switch_list, label="Not Switching", color="orange")

    avg_switch = sum(switch_list)/len(switch_list)
    avg_not_switch = sum(not_switch_list)/len(not_switch_list)

    print("{:45s}: {:.2f}%".format("Average Switching's Winning percentage", avg_switch))
    print("{:45s}: {:.2f}%".format("Average Not Switching's Winning percentage",avg_not_switch))

    plt.axhline(color="r", y=avg_switch, label="Switching's average")
    plt.axhline(color="b", y=avg_not_switch, label="Not Switching's average")

    plt.ylabel('Winning percentage (%)')
    plt.xlabel('Number of trials')

    plt.rcParams['figure.figsize'] = [18, 3]
    plt.legend()
    plt.show()


switch_list = []
not_switch_list = []

generate()
show()