import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Main function"""
    df = load("population_total.csv")

    fr = df.loc[df["country"] == "France"]  # Localize France
    bel = df.loc[df["country"] == "Belgium"]  # Localize Belgium

    fr = fr.iloc[:, 1:242]  # Remove country column
    bel = bel.iloc[:, 1:242]  # Remove country column

    x_title = "Year"
    y_title = "Population"

    # I erased the M from the values
    bel_population = bel.applymap(lambda x: float(x.strip("M")))
    fr_population = fr.applymap(lambda x: float(x.strip("M")))

    years = fr.columns.values.astype(int)
    mask = (years >= 1800) & (years <= 2040)

    fig, ax = plt.subplots()

    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)

    ax.plot(years[mask], bel_population.values[0][mask], label="Belgium")
    ax.plot(years[mask], fr_population.values[0][mask], label="France")

    # Set y-axis tick marks
    ax.set_yticks([3, 14, 28, 40, 70])
    ax.set_yticklabels(["3M", "14M", "28M", "40M", "70M"])

    plt.xticks(range(1800, 2041, 40))
    plt.title("Population Projections")
    plt.legend(loc="lower right")
    plt.show()

    return


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("AssertionError:", e)
        exit()
