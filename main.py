from analysis_functions.import_data import import_data
from analysis_functions.plot_data import plot_data

DATA_FILEPATH = "./data/titanic.csv"

def main():
    print("This is a demonstration of git")
    df = import_data(DATA_FILEPATH)
    plot_data(df, "Pclass", "Survived")
    

if __name__ == "__main__":
    main()