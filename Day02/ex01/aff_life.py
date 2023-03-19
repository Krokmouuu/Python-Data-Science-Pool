import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Main function"""

    df = load("life_expectancy_years.csv")
    tmp = df.loc[df["country"] == "France"]
    tmp = tmp.iloc[:, 1:282]
    x_title = "Year"
    y_title = "Life expectancy"

    years = tmp.columns.values.astype(int)

    # create a mask to filter out years outside of 1800-2080 range
    mask = (years >= 1800) & (years <= 2080)

    plt.plot(years[mask], tmp.values[0][mask])
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.title("France Life expectancy Projections")
    plt.xticks(range(1800, 2081, 40))
    plt.yticks(range(30, 91, 10))
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
