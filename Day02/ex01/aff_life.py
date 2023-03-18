import matplotlib.pyplot as plt
import seaborn as sns
from load_csv import load


def main():
    """Main function"""


    df = load("life_expectancy_years.csv")
    tmp = df.loc[df["country"] == "France"]
    tmp = tmp.loc[tmp["year] >= 2000]
    print(tmp)
    # plt.xlabel(x_title)
    # plt.ylabel(y_title)
    # plt.title("France Life exceptancy Projections")
    plt.show()
    return 0


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("AssertionError:", e)
        exit()
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt:", e)
        exit()