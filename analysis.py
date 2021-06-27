import pandas as pd
import matplotlib.pyplot as plt

def main():
    # read the data
    df = pd.read_csv("export.csv", index_col = 0)
    df = df.drop("2021-06-03 21:51:13", axis = 0)
    
    df.index = pd.DatetimeIndex(df.index)
    print("Correlation Analysis:")
    print(df.corr())
    print("White Noise:")
    print(df.pct_change().std(axis = 0))
    
    # if you dont want minutely data:
    # df = df[::5]

    # # plot
    # fig,ax = plt.subplots(1,1,
    #                     figsize = (15,6))

    # ax.plot(df["Count_original"], label = "Original", color = "tab:orange")
    # ax1 = ax.twinx()
    # ax1.plot(df["Count_LoFi"], label = "LoFi", color = "tab:blue")
    # ax1.legend(loc = "upper right")
    # ax.legend(loc = "upper left")
    # ax.spines["top"].set_visible(False)
    # ax1.spines["top"].set_visible(False)
    # fig.tight_layout()
    # plt.show()
    
    
    fig,ax = plt.subplots(1,1,
                        figsize = (15,6))

    ax.plot(df["Count_original"], label = "Original", color = "tab:orange")
    ax.plot(df["Count_LoFi"], label = "LoFi", color = "tab:blue")
    ax.plot(df["Count_Nature"], label = "Nature", color = "tab:green")
    ax.plot(df.sum(axis = 1), label = "All Viewers", color = "black")
    ax.legend(loc = "upper left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
