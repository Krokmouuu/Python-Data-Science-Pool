from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Main function"""
    df = load("life_expectancy_years.csv")
    df2 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = df.loc[df['1900'] == '1900']
    life = df.iloc[:, 101:102]
    income = df2.loc[df2['1900'] == '1900']
    income = df2.iloc[:, 101:102]

    fig, ax = plt.subplots()
    ax.set_xlabel("Gross domectic product")
    ax.set_ylabel("Life expectancy")

    for i in range(len(income.columns)):
        ax.scatter(income.iloc[:, i], life.iloc[:, i])

    ax.set_yticks([20, 25, 30, 35, 40, 45, 50, 55])
    ax.set_yticklabels([20, 25, 30, 35, 40, 45, 50, 55])
    ax.set_xticks([300, 1000, 10000])
    ax.set_xticklabels(["300", "1k", "10k"])
    plt.title("1900")
    plt.show()
    plt.close()
    return


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("AssertionError:", e)
        exit()
