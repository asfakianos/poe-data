import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

LEAGUES = ("Beastiary","Breach","Delve","Essence","Harbinger","Incursion","Legacy","Legion","Synthesis")

def main():

    plt.title("Exalted Orb price by league")
    plt.xlabel("Days since League Start")
    plt.ylabel("Value in chaos orbs")

    for league in LEAGUES:
        currency = pd.read_csv(f'{league}.currency.csv', sep=";")
        x = currency[(currency["Get"] == 'Exalted Orb') & (currency['Pay'] == 'Chaos Orb')].to_numpy()

        plt.plot(range(0, x[:,4].size),x[:,4], label=league)

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
