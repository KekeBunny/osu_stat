import pandas as pd
import matplotlib.pyplot as plt
from fetch_data import modes


def load_data():
    return pd.read_csv("data.csv")


def show_data(mode: int, data, start: int, end: int):
    plt.xkcd()
    plt.rcParams['figure.figsize'] = (20, 8)
    plt.rcParams['savefig.dpi'] = 300
    plt.rcParams['figure.dpi'] = 300
    plt.title(f"{modes[mode]} pc/pp for #{start} to #{end}")
    plt.xlabel("pc")
    plt.ylabel("pp")
    plt.scatter(data[start - 1:end].pc, data.pp[start - 1:end], s=1)
    plt.show()


if __name__ == "__main__":
    data_demo = load_data()
    show_data(data_demo)
